#!C:\Python27\python.exe
'''
CS1114

Programmer: Samuel Lopez

User Name: SL4506

Submission: rec06.py

This is a python program that will sell three different types of stamps.
Asks for the user name, and only gives change in coins, not dollar bills.
At the end of the program the user is asked to rate the machine; and based
on their response they might be granted a price.

Constraints: NONE

Assumptions: The user will not try to trick us or give us bogus input.

'''
from __future__ import print_function
from MODULE04 import *
from random import *

STAMP74=0.74
STAMP32=0.32
STAMP06=0.06
LOW=0
HIGH=1
totalTimes=0

def welcomeBanner():
    ''' This function displays the welcome banner which welcomes the user into the program'''
    print( "--------------------------------------------" )
    print( " |     Welcome to the snakeStamp Machine!     |" )
    print( " | We dispense only 74, 32 and 6 cent stamps. |" )
    print( " | We give only coins in change - (no bills). |" )
    print( " --------------------------------------------" )
def get_userInput():
    ''' This function asks the user what their first and last name is, and how many stamps they want of each kind'''
    stamp74=int(raw_input("How many 74 cent stamps would you like?"))
    stamp74=verifyPositive(stamp74)
    stamp32=int(raw_input("How many 32 cent stamps would you like?"))
    stamp32=verifyPositive(stamp32)
    stamp06=int(raw_input("How many 6 cent stamps would you like?"))
    stamp06=verifyPositive(stamp06)
    return stamp74,stamp32,stamp06
def verifyPositive(value):
    '''This function check to see if the user entered a postive value for stamps'''
    while value<0:
        print( "Unexpected Value" )
        value=int(raw_input("Please enter a positive value of stamps"))
    return value
def calculateTotalStampPrice(stamp74,stamp32,stamp06):
    ''' This function calculates the total price of all the stamps'''
    totalPrice=(stamp74*STAMP74)+(stamp32*STAMP32)+(stamp06*STAMP06)
    return totalPrice
def printTotal(totalPrice):
    ''' This function prints the total price of all the stamps'''
    print(totalPrice)
def getNumOfDollars():
    ''' This function asks the user how many dollars he or she will be inputting into the machine'''
    numOfDollars=float(raw_input("Please insert amount owed"))
    return numOfDollars
def checkUserMoney(numOfDollars,totalPrice):
    '''This function checks the amount of money the user put in to how much the user owes'''
    while numOfDollars<totalPrice:
        print( "Insufficient Amount. Please insert all of the money" )
        numOfDollars=float(raw_input("Please insert the whole amount or greater"))
    handleTooManyBills(numOfDollars,totalPrice)
    return numOfDollars
def handleTooManyBills(numOfDollars,totalPrice):
    if numOfDollars>totalPrice+1:
        change=numOfDollars-totalPrice
        newChange=(numOfDollars-totalPrice)-int(numOfDollars-totalPrice)
        tip=int(change)
        print ("Thanks for the %i $ tip" % (tip))
        giveChange(newChange)
    else:
        change=numOfDollars-totalPrice
        giveChange(change)
def displayWait():
    '''This function displays a wait message for the user'''
    print( "Thank you. Just a moment please..." )
def giveChange(change):
    ''' This function prints the change in its respective coins'''
    printAsCoins(change)
def prizeMoney(totalPrice):
    ''' This function asks the user for their rating with the program
    and checks to see if they won a prize'''
    userRating=raw_input( "Please rate your experience with this machine using a number between 1 and 10?" )
    if randint(0,1000) == userRating:
        print( "YOU'VE WON THE GRAND PRIZE OF %i DOLLARS" % (50))
    elif (userRating in [2,4,7]) or (17.25<totalPrice<58.42):
        print( "You win %.2f cents" % (2.33))
    elif totalPrice>1.37:
        print( " You won %i cents" % (37))
    else:
        print( " You won %i cents" % (3))
def drawRandomBanner():
    '''This function prints a random banner'''
    firstAndLastLine()
    randomLine('<')
    randomLine('>')
    randomLine('!')
    firstAndLastLine()
def firstAndLastLine():
    ''' This function prints the first and last line of the random banner'''
    print ( "/\\" * 15 )
def getStringSegment():
    '''This function generates a random string segment'''
    character=chr(randint(97,122))
    repeat=randint(4,6)
    segment=character*repeat
    return segment
def randomLine(fillChar):
    '''This function generates a random line for the random banner function'''
    finalStr= ''
    finalStr+= getStringSegment()
    finalStr+= getStringSegment()
    finalStr+= getStringSegment()
    finalStr+= getStringSegment()
    x=30-len(finalStr) if len(finalStr)<30 else 0
    finalStr+=finalStr + fillChar * x
    print(finalStr)
def handleOneCustomer(sumation,maximum,minimum,average):
    stamp74,stamp32,stamp06=get_userInput()
    totalPrice=calculateTotalStampPrice(stamp74,stamp32,stamp06)
    counter+=1
    sumation=totalPrice+sumation
    average=sumation/counter
    if totalPrice>maximum:
        maximum=totalPrice
    if minimum==0 or totalPrice<minimum:
        minimum=totalPrice
    printTotal(totalPrice)
    numOfDollars=getNumOfDollars()
    displayWait()
    checkUserMoney(numOfDollars,totalPrice)
    handleTooManyBills(numOfDollars,totalPrice)
    prizeMoney(totalPrice)
    drawRandomBanner()
    return sumation,maximum,minimum,counter,average
def main():
    sumation=0
    maximum=0
    minimum=0
    counter=0
    average=0
    while LOW<HIGH:
        firstName=raw_input("What is your first name?")
        lastName=raw_input("What is your last name?")
        if (firstName == "MAINTENANCE" ) and (lastName == "MANAGERXYZ" ):
            print( "Do your maintenance work, and DO NOT forget to restart this program" )
            print( "The program ran %i times since last check " % (counter))
            print( "The highest was %i " % (maximum))
            print( "The lowest was %i " % (minimum))
            print( "The sumation was %i " % (sumation))
            print( "The average was %i " % (average))
            break
        else:
            sumation,maximum,minimum,counter,average=handleOneCustomer(sumation,maximum,minimum,counter,average)
if __name__== "__main__":
    main()


    
    


