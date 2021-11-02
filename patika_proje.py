## Soru - 1
from typing import List

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list2 = []

def lookInside(l):                  # Takes the list type element
    for x in l:                     # For each sub-element of it
        if type(x) is not list:     # If the sub-element is not list, 
            flat_list2.append(x)    # Then add it to flat_list
        else:                       
            lookInside(x)           # Else, look inside of it again

def makeFlat(l):                    # Getting the list 
    for e in l:                     # Checking the elements of the list
        if type(e) is list:         # If element's type is list then
            lookInside(e)           # send that element to lookInside function 
        else:
            flat_list2.append(e)    # Else, (if it is not list) append it to our new flat_list

makeFlat(l)                         # Function call, the complex list has been given to function
print(flat_list2)                   # Printing the flatten list

## Soru - 2

list2 = [[1, 2], [3, 4], [5, 6, 7]]
list1 = list2[::-1]

print(list1)
