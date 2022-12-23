# Write a Python program to check a given list of integers where the sum of the first i integers is i. 


def sumOfAll(nums):
    return sum(nums[:len(nums)])


list1 = [0, 1, 2, 3, 4, 5]
print(sumOfAll(list1))
list2 = [1, 1, 1, 1, 1, 1]
print(sumOfAll(list2))
list3 = [2, 2, 2, 2, 2] 
print(sumOfAll(list3))

