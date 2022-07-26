# **Harvard's CS50P: Final Project**

# Cocktail Recipe Generator in Python

### **Requirements**

Once you have solved each of the course’s problem sets, it’s time to implement your final project, a Python program of your very own! The design and implementation of your project is entirely up to you, albeit subject to these requirements:

- Your project must be implemented in Python.
- Your project must have a main function and at least three other functions, each of which must be accompanied by tests that can be executed with pytest.
- Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project.
- Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).
- Your test functions must be in a file called test*project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test* (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).
- You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement.
- Implementing your project should entail more time and effort than is required by each of the course’s problem sets.
- Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project.
  <br>
  <br>

### **Video Demo**:

<https://youtu.be/yOuZJMAFPTs>

### **Installation:**

- Install project dependencies by running pip install -r requirements.txt.
- Run the python program with command 'python project.py'.

### **Building tools:**

-Python  
-External libraries: [PYFiglet](https://pypi.org/project/pyfiglet/0.7/), [RICH](https://pypi.org/project/rich/), [TheCocktailDB API](https://www.thecocktaildb.com/), [FPDF2](https://pypi.org/project/fpdf2/)
<br>

### **Project description**

For my final CS50P project, the initial idea was to create a program that used an API in order to work. So, after doing a little research, I decided to develop a python based CLI application to generatescocktail recipes according to the user's preferences, using the 'TheCocktailDB' JSON API, a free and "open, crowd-sourced database of drinks and cocktails from around the world."

In order to make the experience visually prettier and more functional, I used the RICH library to stylize the colors and font weights of the python console.

When the application is ran, the user is prompted to follow two different paths: search the recipe by the cocktail's name (if already decided which one they want), or provide a list of ingredients he intends to use.
In the first case, a query is made to the API and:

- If there are no cocktails in the DB matching that name, a message is returned asking the user to input another name.
- If there is 1 result only, then the app displays the recipe for the cocktail.
- If more than 1 result is shown, the user needs to choose the cocktail and then gets the recipe. (i.e.: looking up 'screwdriver' returns 2 different cocktails: 'Scredriver' and 'Rum Screwdriver')

In similar spirit, if the user chooses to search by ingredient, the flow is like so:

- If an unknown ingredient is in the list of ingredients submitted by the user, a message is returned saying that is a non-existent item.
- If the ingredients only match 1 cocktail, then it automatically displays the recipe for it.
- If more than one cocktail uses the ingredients, a list is shown, and the user must select one.
- If no matches are found, the user is asked to provide another list.

In all of the cases above, after the recipe is found and displayed on the console, a PDF is generated with all the information in a styled layout. The file is saved in the root folder and, if the file already exists and is opened, the _PermissionError_ is catched, and a message is displayed asking the user to close the file and press 'ENTER' to try and save it again.

On every step of the process, after the user input, the _cls()_ function is called, which clears the screen and prints the title before the next question, to give the illusion of a fixed title throughout the whole application.

The 'search by ingredient' feature was a tricky one to solve, as the free key for the API only provides a _single_ ingredient search method. The solution found in this case was to make a query for each ingredient, and storing each resulting list nested inside another list, and then check for the intersection between its items.

<br>

### **Files and directories**

- `fonts/` - contains project typefaces
- `background-01.png` - PDF background
- `project.py` - main project file
- `test_project.py` - pytest project file
