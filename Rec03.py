#!C:\Python27\python.exe

'''
CS1114

Submission: Rec03.py

Programmer: Samuel Lopez
Username: SL4506

This program will welcome the user, ask the user how many dougnuts
and coffees he or she would like, calculate the total of the two with tax,
and print the receipt.

Parameters:

Assumptions: NONE

Constraints: NONE

'''

from __future__ import print_function
import os

COST_OF_COFFEE=0.77
COST_OF_DOUGHNUT=0.64
TAX_RATE=0.0846

def displayWelcome():
    ''' This function will print the welcome statement to the screen'''
    print("/\\" * 15)
    print("Welcome to the Coffee and Doughnut Shoppe")
    print("/\\" * 15)
def getNumOfCoffee():
    '''Asks the user the amount of cups of coffee they would like'''
    numOfCoffee=int(raw_input("How many cups of coffee would you like?"))
    return numOfCoffee
def getNumOfDoughnuts():
    '''Asks the user the amount of doughnuts they would like'''
    numOfDoughnuts=int(raw_input("How many doughnuts would you like?"))
    return numOfDoughnuts
def getOrder():
    '''Calls the getNumOfCoffee function and the getNumOfDoughnuts function and stores what they return'''
    numOfCoffee=getNumOfCoffee()
    numOfDoughnuts=getNumOfDoughnuts()
    return numOfCoffee,numOfDoughnuts
def coffeeCost(numOfCoffee):
    '''Calculates the total cost of the coffee'''
    totalCoffeeCost=numOfCoffee*COST_OF_COFFEE
    return totalCoffeeCost
def doughnutCost(numOfDoughnuts):
    '''Calculates the total cost of the doughnuts'''
    totalDoughnutCost=numOfDoughnuts*COST_OF_DOUGHNUT
    return totalDoughnutCost
def calculateTax(totalDoughnutCost,totalCoffeCost):
    '''Calculates the tax of the doughnuts and coffee cups'''
    totalTax=TAX_RATE*(totalDoughnutCost+totalCoffeCost)
    return totalTax
def calculateTotal(totalDoughnutCost,totalCoffeeCost,totalTax):
    '''Calculates the entire total of the doughnuts and coffee cups plus tax'''
    totalAmount=totalDoughnutCost+totalCoffeeCost+totalTax
    return totalAmount
def displayBill(numOfCoffee,numOfDoughnuts,totalCoffeeCost,totalDoughnutCost,totalTax,totalAmount):
    print( "%i cups of coffee: $ %.2f" % (numOfCoffee,totalCoffeeCost))
    print( "%i doughnuts: $ %.2f" % (numOfDoughnuts,totalDoughnutCost))
    print( "tax : $ %.2f" % (totalTax))
    print( "Amount Owed : $ %.2f" % (totalAmount))
    print( "Thank you for buying local!! :)" )
def main():
    displayWelcome()
    numOfCoffee,numOfDoughnuts=getOrder()
    totalCoffeeCost=coffeeCost(numOfCoffee)
    totalDoughnutCost=doughnutCost(numOfDoughnuts)
    totalTax=calculateTax(totalDoughnutCost,totalCoffeeCost)
    totalAmount=calculateTotal(totalDoughnutCost,totalCoffeeCost,totalTax)
    displayBill(numOfCoffee,numOfDoughnuts,totalCoffeeCost,totalDoughnutCost,totalTax,totalAmount)
    os.system("pause")
if __name__=="__main__":
    main()

    
    
    



