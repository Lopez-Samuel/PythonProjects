def main():
    totalSum=calculateSum(number)
    divBy3(totalSum)
def calculateSum(number):
    'This function calculates the sum of the individual digits of any given number'
    if number<10:
        return number
    else:
        lastDigit=number%10
        sumNumber=0
        count=0
        while number !=0:
            number=(number/10)
            temp1=(number%10)
            sumNumber=temp1+sumNumber
            count=count+1
    totalSum=lastDigit+sumNumber
    return totalSum
def divBy3(totalSum):
    'Checks to see if the total sum is divisible by 3'
    if totalSum%3==0:
        print True
    else:
        print False
    

main()
