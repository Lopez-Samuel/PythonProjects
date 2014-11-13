#!C:\Python27\python.exe
'''
CS1114

Programmer: Samuel Lopez

User Name: SL4506

Submission: hw08.py

Constraints: NONE

'''
import copy
from __future__ import print_function

def displayListElements( list1 ):
    '''Displays each item in a list on a different line'''
    for x in list1:
        print ( x )

def returnMinValue( list1 ):
    '''Returns the lowest value number in a list'''
    list1.sort()
    return list1[0]

def returnMinValueIndex( list1 ):
    '''Returns the postion of the lowest value in a list'''
    miniValue = list1[0]
    for value in list1:
        if value < miniValue:
            miniValue = value
    return list1.index( miniValue )

def removeValuesFromList(listName,start,end):
    '''Takes a list, a lower bound, and upper bound, and removes the numbers between these values from the list'''
    n=1
    while (start+n) < (end):
        listName.remove(start+n)
        n+=1
    return(listName)
def commonElements(list1,list2):
    '''Takes two lists and finds the common elements and returns them in a list'''
    common=[]
    for elem in list1:
        if elem in list2:
            if elem not in common:
                common.append(elem)
    return(common)
def insertListIntoOrder(list1,list2):
    '''Takes two lists and inserts the second list, into the first list after it was sorted and reversed'''
    copyList1=copy.deepcopy(list1)
    copyList1.sort()
    copyList1.reverse()
    mini=list2[0]
    n=0
    print(copyList1)
    while copyList1[n] > mini:
        n+=1
    copyList1.insert(n,list2)
    return(copyList1)
        
