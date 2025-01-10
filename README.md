# Nuclues Calculator
#### Video Demo:  _URL [HERE](https://drive.google.com/file/d/1t5XF8UeFY5lEnYBGX3RlzerFLz7et9O8/view?usp=drive_link)_
#### Description:
Nucleus Calculator is a scientific calculator I built using a combination of HTML, CSS, JavaScript for the frontend, and Python for the backend, utilizing the Python Eel library and an SQLite3 database for logging user inputs. This calculator was designed not only to perform basic calculations but also to handle more complex mathematical expressions, such as those involving nested parentheses or multiple operations with different levels of precedence. The unique aspect of this project is that it doesn’t rely on built-in functions from Python or JavaScript to perform the calculations; instead, it uses custom-built recursive functions and a parser developed in Python to evaluate expressions from scratch. This approach ensured that the entire calculation process was transparent, giving me full control over the logic behind it. For instance, when a user enters a mathematical expression like “(5 + 3) * (12 / 4)”, the input is parsed and evaluated step by step without depending on any predefined functions to process the operations. The Python code does the heavy lifting, breaking down the expression and executing the operations in the correct order. On top of the core calculation features, Nucleus Calculator includes a history log that tracks the last 10 calculations made by the user, which is displayed on the main interface for quick reference. In addition to this, there is a settings section where the user can access up to the most recent 100 logs. These logs are stored in a lightweight SQLite3 database, ensuring they are persistent and easy to retrieve whenever needed, all while maintaining fast performance. The idea behind including this feature was to provide users with a way to review their past calculations without needing to re-enter them. This is especially useful for those who perform complex calculations that require multiple steps, as they can always go back to previous results without starting from scratch. One of the most important design choices I made for this project was to ensure it could be used as a standalone desktop application. Instead of relying on a server-client architecture with frameworks like Flask, I opted for Python Eel. This library bridges Python with web technologies, allowing me to build a web-like interface that could be packaged as a desktop app. The result is that users can run the calculator directly on their computers without needing to install a web server or rely on an internet connection. They simply download the executable file and run it just like any other desktop application. This is a crucial feature because it makes the app much more accessible to a broader audience. From a technical perspective, the frontend was built using basic HTML, CSS, and JavaScript to provide a clean and simple user interface. HTML handles the structure, CSS ensures the app looks visually appealing, and JavaScript adds interactivity, ensuring a smooth and responsive user experience. The calculator’s functionality is powered by Python, which handles the heavy lifting in terms of evaluating mathematical expressions. This integration of frontend and backend technologies made the project an interesting challenge and a great learning experience. Although Nucleus Calculator is fully functional in its current form, I plan to continue improving it in the future. Some ideas for future enhancements include adding graphing capabilities for visualizing functions and extending the range of supported mathematical functions to cover more advanced topics. There is also potential for customization, such as offering different themes or allowing users to personalize the interface to suit their preferences. Overall, Nucleus Calculator is a tool that not only serves a practical purpose but also represents the culmination of many technical decisions, all aimed at creating a tool that is both powerful and easy to use. The ability to perform complex calculations, store logs, and function as a standalone desktop application makes it a valuable addition to anyone’s toolbox, and I’m excited to continue developing it in the future.

## How to use
First, open your Chrome browser. Python Eel uses a Chrome instance for every app, to allow connections between the frontend and the backend.

Then simply, execute the following in your terminal:
```bash
python Nucleus.py
# or
python3 Nucleus.py
```

From here, you can use the calculator easily. Note that the calculator is tested, and does return actually accurate results.

Please also note that if you close the window, the application will be _permanently stopped_ and you will need to **re-execute the start command** above.

### Developer's note
I, Parsa Sabet, have created and designed the Nucleus Calculator.
The entire codebase is written by myself, with little help to complete the parser from the internet. No AI was used in the creation process or testing of this basic application, and no other individuals or groups have helped me complete it directly.
I have searched through the internet with the problems that I've had but no blocks of the code were shared and no help was asked for.
Thank you for respecting the license of this application, and using this calculator.

---
<br>
Parsa Sabet, <br>
January 10, 2025
