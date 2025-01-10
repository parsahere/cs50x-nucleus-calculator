import func_computation

# CODE WRITTEN BY PARSA SABET

def numeric_meval(user_expression:str):
    try:
        return func_computation.Func_Computation(user_expression)
    except:
        return 'error'