#!C:\Python27\python.exe
'''
CS1114

Programmer: Samuel Lopez

User Name: SL4506

Submission: rec09.py

Constraints: NONE

Assumptions: The user will not try to trick us or give us bogus input.

'''
AVAILABLE_LIST=["milk", "chocolate covered cherries", "apple", "orange", "banana", "corn on the cob", "kampyo sushi", "asparagus", "avacado", "alfalfa", "acorn squash", "almond package", "arugala bunch", "artichoke", "applesauce", "wasabi", "udon noodles", "tunafish can", "apple juice", "avocado sushi", "bruscetta", "bagel", "barley", "bisque", "bluefish", "bread", "broccoli", "buritto", "babaganoosh", "cabbage", "chocolate cake", "red velvet cake", "strawberry short cake", "carrots", "celery", "cheese", "catfish", "chowder", "clams", "coffee", "corn", "crab", "curry", "cereal", "chimichanga", "dumpling", "donut", "egg", "enchilada", "eggroll", "english muffin", "edimame", "eelSushi", "o toro sashimi", "fajita", "falafel", "fondu", "french toast", "french dip", "garlic", "ginger", "gnocchi", "granola", "grape", "green bean", "guacamole", "gumbo", "grits", "graham crackers", "halibut", "honey", "huenos rancheros", "hash browns", "hummus", "chocolate ice cream", "strawberry ice cream", "cherry garcia ice cream", "puri", "veggie kurma", "jambalaya", "kale", "ketchup", "kiwi", "kidney beans pckg", "great northern beans pckg", "lobster", "linguine", "lasagna", "pepperoni pizza", "mushroom pizza", "pancakes", "quesadilla", "quiche", "spinach", "spaghetti", "tater tots", "toast", "waffles", "walnuts", "peanuts", "hazelnuts", "cranberries", "yogurt", "ziti", "zucchini", "canteloupe", "figs", "salt", "pepper", "nutmeg", "yucca", "shichimi"]
NO_BUY_LIST=[]
SHOPPING_LIST=[]
FINAL_LIST=[]
def getUserInput():
    shoppingListInput=raw_input( "What item would you like to add to the shopping list" )
    return shoppingListInput
def generateShoppingList():
    sentinel="SHOP"
    shoppingListInput=raw_input( "What item would you like to add to the shopping list" )
    while shoppingListInput != sentinel:
        validateUserInput(shoppingListInput)
        shoppingListInput=getUserInput()
    printShoppingList()
def generateNoBuyList():
    inputtedValue=raw_input("What item would you not want to be added to the no buy list")
    inputtedValue.lower()          
    if noDoubles(inputtedValue)== True:
        print( "This item is already in the no buy list" )
    elif inputtedValue not in AVAILABLE_LIST:
        print ( " This item is not in the available shopping list from the store" )
    else:
        NO_BUY_LIST.append(inputtedValue)
        print( "Item added to no buy list" )
        
def noDoubles(inputtedValue):
    return(inputtedValue in NO_BUY_LIST)
def validateUserInput(value):
    if value in NO_BUY_LIST:
        print( "This value cannot be added to shopping list since it is in the no buy list" )
    elif value not in AVAILABLE_LIST:
        print( " This value is not on the list of available items at the store" )
    else:
        SHOPPING_LIST.append(value)
        print( "%s added to shopping list" % (value))
def printNoBuyList():
    for x in NO_BUY_LIST:
        print( x )
def printShoppingList():
    SHOPPING_LIST.sort()
    while len(SHOPPING_LIST)!= 0:
        temp=SHOPPING_LIST[0]
        counter=SHOPPING_LIST.count(temp)
        FINAL_LIST.append([temp, counter])
        for i in range(counter):
            SHOPPING_LIST.remove(temp)
    for x in FINAL_LIST:
        print( x )
def menu():
    choice=int(raw_input("Please select between \n 1.Add an item to the shopping list \n 2.Create the I wont buy list \n 3.Display an alphabetic list of all available foods \n 4.Quit and print shopping list in alphabetical order"))
    if choice == 1:
        generateShoppingList()
    elif choice == 2:
        printNoBuyList()
    elif choice == 3:
        AVAILABLE_LIST.sort()
        print( AVAILABLE_LIST )
    elif choice==4:
        printShoppingList()
def main():
    while 1>0:
        menu()
main()

    
