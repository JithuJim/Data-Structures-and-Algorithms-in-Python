#Write a Python program that can make change. Your program should
#take two numbers as input, one that is a monetary amount charged and the
#other that is a monetary amount given. It should then return the number
#of each kind of bill and coin to give back as change for the difference
#between the amount given and the amount charged. The values assigned
#to the bills and coins can be based on the monetary system of any current
#or former government. Try to design your program so that it returns as
#few bills and coins as possible.

def give_back_amount(given,charged):
    coins = [1,5,10,25,50,100,200,500,1000,2000,5000,10000]
    give_back = (given - charged) * 100
    result = {ele:0 for ele in coins}
    for ele in list(reversed(coins)):
        count = 0
        while(give_back >= ele):
            count +=1
            give_back = give_back - ele
        result[ele] = count
    return result

print give_back_amount(10,.25)

