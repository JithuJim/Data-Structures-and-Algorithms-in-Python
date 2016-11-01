#Write a Python program that can take a positive integer greater than 2 as
#input and write out the number of times one must repeatedly divide this
#number by 2 before getting a value less than 2.

def divide_by_2(inp):
    if inp == 2:
        return 1

    if inp <2 :
        return 0
    count = 0

    while(inp>=2):
        inp = inp//2
        count += 1
    return count

print divide_by_2(2)

