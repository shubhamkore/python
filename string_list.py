# Write a Python program find the longest string of a given list of strings. 


def maxString(strings):
    max_str = strings[0]
    for x in strings:
        if len(x) > len(max_str):
            max_str = x
    return max_str


list1 = ['cat', 'car', 'fear', 'center']
list2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']

result1 = maxString(list1)
print("The longest string is - \t " + result1)
result2 = maxString(list2)
print("The longest string is  - \t" + result2)

