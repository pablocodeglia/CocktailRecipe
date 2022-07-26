from unicodedata import name
import requests, sys, re, os
from rich.console import Console
from rich.theme import Theme
from pyfiglet import Figlet
from fpdf import FPDF


# RICH console setup
rich_custom_theme = Theme({"def":"white", "inp":"magenta bold", "st1":"cyan bold italic", "st2":"yellow bold","st3":"green bold","st4":"red bold"})
console = Console(theme=rich_custom_theme)

def main():
    cls()
    while True:
        cls()
        try:
            console.print("Welcome!", style="st1")
            console.print("Do you know the name of the drink, or do you want to search by ingredients?\n", style="inp")
            choice = int(console.input("[inp]1.[/inp] I know the cocktail's name!\n[inp]2.[/inp] No idea! I want to search by ingredients!\n"))

            if choice == 1:
                cls()
                display_recipe(search_by_name())
            elif choice ==2:
                cls()
                display_recipe(search_by_ingredient())
        except ValueError:
            pass

def cls():
    # Quick function to clear the console
    os.system('cls' if os.name=='nt' else 'clear')

    # Displays Title
    f = Figlet(font='kban')
    title_text = f.renderText('Cocktail Recipe Generator')
    console.print(f'[st2]{title_text}[/st2]')


def query_input_info(item,type_of_search,name):
    url = f"http://www.thecocktaildb.com/api/json/v2/9973533/{type_of_search}.php"
    querystring = {f"{item}":name}
    response = requests.request("GET", url,params=querystring)
    query = response.json()

    return query['drinks']

def search_by_name():
    cls()
    while True: 
        cocktail_name = console.input("\n[inp]What's the name of the cocktail you are looking for? [/inp]\n")
        query = query_input_info("s","search",cocktail_name)

        if query == None:
            cls()
            console.print("[st2]There are no cocktails with that name in the database! 😕[/st2]")
        elif len(query) == 1:
            return query[0]['strDrink']

        elif len(query) > 1:
            cls()
            while True:
                console.print("[inp]These are all the cocktails matching that name!\nWhich one do you want to know the recipe for?\n[/inp]")
                for item in query:
                    index = query.index(item)
                    console.print(f"[inp]{index+1}.[/inp] {query[index]['strDrink']}")

                try:
                    choice = int(console.input("\n[inp]Select the number of the cocktail you want:[/inp]")) - 1
                    return query[choice]['strDrink']
                    
                except IndexError:
                    cls()
                    console.print("[st2]Mmmm... That's not a valid choice! [/st2]⚠️")
                    pass
            
def search_by_ingredient():

    ingredients = (console.input("\n[inp]List all the ingredients, separated by a coma (','):[/inp]\n")).split(',')
    ingredients = [n.strip() for n in ingredients]

    '''
    Make a query for each ingredient, then add each result as a list inside the 'ingredients_results' list, and check for the intersection between
    them to get the recipes with all ingredients.
    '''
    ingredients_query_nested_list = []

    for i in range(len(ingredients)):
        # Request results for each ingredient
        query = query_input_info("i","filter",ingredients[i])

        if query == "None Found":
            cls()
            console.print(f'[inp]Could not find any cocktail using "{ingredients[i]}". Are you sure that\'s a thing?[/inp] 🤔')
            search_by_ingredient()
        
        cocktails_n = []
        for drink in query:
            cocktails_n.append(drink['strDrink'])
        # Append to the complete list
        ingredients_query_nested_list.append(cocktails_n)
    
    # Check for the cocktails in which all ingredients are present
    results_overlap = sorted(list(set.intersection(*map(set,ingredients_query_nested_list))))

    if len(results_overlap) == 0:
        cls()
        console.print("No cocktails found with all those ingredients! 🤷 Try another combination! ", style="st2")
        search_by_ingredient()

    elif len(results_overlap) == 1:
        return results_overlap[0]

    elif len(results_overlap) > 1:
        cls()
        while True:
            console.print(f"\n[inp]These are the cocktails using those ingredients:[/inp]")
            for result in results_overlap:
                index = results_overlap.index(result)
                console.print(f'[inp]{index+1}.[/inp] {result}')

            try:
                choice = int(console.input("\n[inp]Select the number of the cocktail you want:[/inp]")) - 1
                return results_overlap[choice]

            except IndexError:
                cls()
                console.print("[st2]Mmmm... That's not a valid choice! [/st2]⚠️")
                pass
            
def display_recipe(cocktail):
    cls()
    
    query = (query_input_info("s","search",cocktail))[0]
    ingredients = get_formatted_ingredient_dict(query)
    
    recipe_str = ''
    recipe_str += f"\n🍹[inp] {query['strDrink']} [/inp]🍸\n"
    recipe_str += f"[st1]\nIngredients:\n[/st1]"
    for k,v in ingredients.items():
        recipe_str += f"[def]{v} {k}[/def]\n"
    recipe_str += f"[st1]\nInstructions:\n[/st1]"
    recipe_str += f"{query['strInstructions']}\n"

    console.print(recipe_str)

    create_pdf(query,ingredients)
    
def get_formatted_ingredient_dict(cocktail):
    ingredient = []
    measure = []
    for k,v in cocktail.items():
        if k.startswith("strIngredient") and v is not None:
            ingredient.append(v)
        if k.startswith("strMeasure") and v is not None:
            measure.append(v)

    return dict(zip(ingredient,measure))

def create_pdf(query,ingredients):
    ingredients_str=""
    for k,v in ingredients.items():
            ingredients_str += v + k + " | "

    pdf = FPDF(orientation="L", unit="mm", format=(100, 200))
    pdf.set_margin(0)
    pdf.add_page()


    pdf.image('images/background-01.png', w=200, h=100, x=0, y=0)
    pdf.image(query['strDrinkThumb'], h=70, w=70, x=00, y=15)
    pdf.add_font("Brandon_reg_it", "", "fonts/Brandon_reg_it.ttf")
    pdf.add_font("Brandon_med", "", "fonts/Brandon_med.ttf")
    pdf.set_y(10)
    pdf.set_x(75)

    # Name
    pdf.set_text_color(r=75 , g=196, b=214)
    pdf.set_font("Brandon_reg_it", "", 26)  
    pdf.cell(90, 8, query['strDrink'], new_x="LEFT", new_y="NEXT", align='L')

    # Glass
    pdf.set_text_color(r=205 , g=70, b=100)
    pdf.set_font("Brandon_med", "", 10)  
    pdf.set_x(75)
    pdf.cell(60, 5, "Glass:", new_x="LEFT", new_y="NEXT", align='L')
    pdf.set_text_color(r=30 , g=170, b=90)
    pdf.set_x(80)
    pdf.cell(60, 5, query['strGlass'], new_x="LEFT", new_y="NEXT", align='L')

    # Ingredients
    pdf.set_text_color(r=205 , g=70, b=100)
    pdf.set_font("Brandon_med", "", 10)  
    pdf.set_x(75)
    pdf.cell(60, 5, "Ingredients:", new_x="LEFT", new_y="NEXT", align='L')
    pdf.set_text_color(r=30 , g=170, b=90)
    pdf.set_x(80)
    pdf.multi_cell(115, 4, ingredients_str, new_x="LEFT", new_y="NEXT", align='L')

    # Text
    pdf.set_text_color(r=205 , g=70, b=100)
    pdf.set_font("Brandon_med", "", 10)  
    pdf.set_x(75)
    pdf.cell(60, 5, "Instructions:", new_x="LEFT", new_y="NEXT", align='L')
    pdf.set_text_color(r=30 , g=170, b=90)
    pdf.set_x(80)
    pdf.multi_cell(105, 4, query['strInstructions'], new_x="LEFT", new_y="NEXT", align='L')
    
    while True:
        try:
            filename = f"Cocktail Recipe - {query['strDrink']}.pdf"
            pdf.output(filename)
            console.print("[st3]PDF GENERATED![/st3]")
        except PermissionError:
            console.input('[st4]The file you are trying to save is already opened, close it and press "ENTER" to try again[/st4]')
        else:
            continue_or_exit()

def continue_or_exit():
    
    response = console.input('\n[st2]Do you want to look for another recipe?[/st2] [Y/N]\n')
    while True:
        try:
            if response.upper() == "Y":
                main()
            elif response.upper() == "N":
                sys.exit()
        except ValueError:
            console.input('[st4]Invalid Option[/st4]')



    



if __name__ == "__main__":
    main()