from project import query_stuff, search_by_ingredient, search_by_name, get_formatted_ingredient_dict
from pytest import MonkeyPatch

def test_query_stuff():
    
    assert (query_stuff("s","search","Bloody Mary"))[0]['strDrink'] == "Bloody Mary"
    assert len(query_stuff("s","search","Margarita")) == 6

def test_search_by_name():
    monkeypatch = MonkeyPatch()
    answers = iter(["margarita","1"])
    monkeypatch.setattr('builtins.input', lambda: next(answers))
    assert search_by_name() == "Margarita"

    monkeypatch = MonkeyPatch()
    answers = iter(["mojito","3"])
    monkeypatch.setattr('builtins.input', lambda: next(answers))
    assert search_by_name() == "Mango Mojito"

    monkeypatch = MonkeyPatch()
    answers = iter(["bloody mary"])
    monkeypatch.setattr('builtins.input', lambda: next(answers))
    assert search_by_name() == "Bloody Mary"

def test_search_by_ingredient():
    monkeypatch = MonkeyPatch()
    answers = iter(["lime, cachaca, demerara sugar"])
    monkeypatch.setattr('builtins.input', lambda: next(answers))
    assert search_by_ingredient() == "Dark Caipirinha"
   
    monkeypatch = MonkeyPatch()
    answers = iter(["lime, cachaca","2"])
    monkeypatch.setattr('builtins.input', lambda: next(answers))
    assert search_by_ingredient() == "Dark Caipirinha"

def test_get_formatted_ingredient_dict():

    dict = {"idDrink":"11007","strDrink":"Margarita","strDrinkAlternate":None,"strTags":"IBA,ContemporaryClassic","strVideo":None,"strCategory":"Ordinary Drink","strIBA":"Contemporary Classics","strAlcoholic":"Alcoholic","strGlass":"Cocktail glass","strInstructions":"Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.","strInstructionsES":None,"strInstructionsDE":"Reiben Sie den Rand des Glases mit der Limettenscheibe, damit das Salz daran haftet. Achten Sie darauf, dass nur der \u00e4u\u00dfere Rand angefeuchtet wird und streuen Sie das Salz darauf. Das Salz sollte sich auf den Lippen des Genie\u00dfers befinden und niemals in den Cocktail einmischen. Die anderen Zutaten mit Eis sch\u00fctteln und vorsichtig in das Glas geben.","strInstructionsFR":None,"strInstructionsIT":"Strofina il bordo del bicchiere con la fetta di lime per far aderire il sale.\r\nAvere cura di inumidire solo il bordo esterno e cospargere di sale.\r\nIl sale dovrebbe presentarsi alle labbra del bevitore e non mescolarsi mai al cocktail.\r\nShakerare gli altri ingredienti con ghiaccio, quindi versarli delicatamente nel bicchiere.","strInstructionsZH-HANS":None,"strInstructionsZH-HANT":None,"strDrinkThumb":"https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg","strIngredient1":"Tequila","strIngredient2":"Triple sec","strIngredient3":"Lime juice","strIngredient4":"Salt","strIngredient5":None,"strIngredient6":None,"strIngredient7":None,"strIngredient8":None,"strIngredient9":None,"strIngredient10":None,"strIngredient11":None,"strIngredient12":None,"strIngredient13":None,"strIngredient14":None,"strIngredient15":None,"strMeasure1":"1 1/2 oz ","strMeasure2":"1/2 oz ","strMeasure3":"1 oz ","strMeasure4":None,"strMeasure5":None,"strMeasure6":None,"strMeasure7":None,"strMeasure8":None,"strMeasure9":None,"strMeasure10":None,"strMeasure11":None,"strMeasure12":None,"strMeasure13":None,"strMeasure14":None,"strMeasure15":None,"strImageSource":"https://commons.wikimedia.org/wiki/File:Klassiche_Margarita.jpg","strImageAttribution":"Cocktailmarler","strCreativeCommonsConfirmed":"Yes","dateModified":"2015-08-18 14:42:59"}
    assert get_formatted_ingredient_dict(dict) == {'Tequila': '1 1/2 oz ', 'Triple sec': '1/2 oz ', 'Lime juice': '1 oz '}

    dict = {'idDrink': '11113', 'strDrink': 'Bloody Mary', 'strDrinkAlternate': None, 'strTags': 'IBA,ContemporaryClassic', 'strVideo': None, 'strCategory': 'Ordinary Drink', 'strIBA': 'Contemporary Classics', 'strAlcoholic': 'Alcoholic', 'strGlass': 'Old-fashioned glass', 'strInstructions': 'Stirring gently, pour all ingredients into highball glass. Garnish.', 'strInstructionsES': None, 'strInstructionsDE': 'Unter leichtem Rühren alle Zutaten in ein Highball-Glas geben. Garnieren.', 'strInstructionsFR': None, 'strInstructionsIT': 'Mescolando delicatamente, versare tutti gli ingredienti nel bicchiere highball.', 'strInstructionsZH-HANS': None, 'strInstructionsZH-HANT': None, 'strDrinkThumb': 
            'https://www.thecocktaildb.com/images/media/drink/t6caa21582485702.jpg', 'strIngredient1': 'Vodka', 'strIngredient2': 'Tomato juice', 'strIngredient3': 'Lemon juice', 'strIngredient4': 'Worcestershire sauce', 'strIngredient5': 'Tabasco sauce', 'strIngredient6': 'Lime', 'strIngredient7': None, 'strIngredient8': None, 'strIngredient9': None, 'strIngredient10': None, 'strIngredient11': None, 'strIngredient12': None, 'strIngredient13': None, 'strIngredient14': None, 'strIngredient15': None, 'strMeasure1': '1 1/2 oz ', 'strMeasure2': '3 oz ', 'strMeasure3': '1 dash ', 'strMeasure4': '1/2 tsp ', 'strMeasure5': '2-3 drops ', 'strMeasure6': '1 wedge ', 'strMeasure7': None, 'strMeasure8': None, 'strMeasure9': None, 'strMeasure10': None, 'strMeasure11': None, 'strMeasure12': None, 'strMeasure13': None, 'strMeasure14': None, 'strMeasure15': None, 'strImageSource': 'https://www.thecocktaildb.com/drink/11113-Bloody-Mary', 'strImageAttribution': 'TheCocktialDB.com', 'strCreativeCommonsConfirmed': 'Yes', 'dateModified': '2015-08-18 15:09:14'}
    assert get_formatted_ingredient_dict(dict) == {'Vodka': '1 1/2 oz ', 'Tomato juice': '3 oz ', 'Lemon juice': '1 dash ', 'Worcestershire sauce': '1/2 tsp ', 'Tabasco sauce': '2-3 drops ', 'Lime': '1 wedge '}
