import sqlite3

# connect to SQLite3 database
conn = sqlite3.connect('logs.db')
cursor = conn.cursor()

# create a table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expression TEXT,
    result TEXT,
    exp_date_time TEXT
)
''')
conn.commit()

def count_file_logs():
    cursor.execute('SELECT COUNT(*) FROM logs')
    lines = cursor.fetchone()[0]
    if lines >= 101:
        cursor.execute('DELETE FROM logs WHERE id IN (SELECT id FROM logs ORDER BY id LIMIT 1)')
        conn.commit()
    return lines

log_lines = count_file_logs()

def get_date_expression(exp_date_time, expression, result, run_count):
    latest_log = (expression, result, exp_date_time)
    cursor.execute('INSERT INTO logs (expression, result, exp_date_time) VALUES (?, ?, ?)', latest_log)
    conn.commit()
    count_file_logs()

def pick_last_10():
    cursor.execute('SELECT expression, result, exp_date_time FROM logs ORDER BY id DESC LIMIT 10')
    last_10 = cursor.fetchall()
    return [f'Expression: {row[0]} = {row[1]}  ,  On: {row[2]}' for row in last_10]

def pick_all():
    cursor.execute('SELECT expression, result, exp_date_time FROM logs')
    all_logs = cursor.fetchall()
    return [f'Expression: {row[0]} = {row[1]}  ,  On: {row[2]}' for row in all_logs]

# Close the connection when done
def close_connection():
    conn.close()