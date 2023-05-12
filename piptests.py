# Write a Python program that takes a list of strings as input and outputs 
# the number of times each string appears in the list, using a dictionary and conditional statements.
strings = ['apple', 'banana', 'orange', 'apple', 'banana', 'pear', 'apple']
counts = {}
for s in strings:
    if s in counts:
        counts[s] += 1
    else:
        counts[s] = 1
for s, count in counts.items():
    print(s, count)


# Write a Python program that takes a list of numbers as input and outputs the median of the numbers 
def calculate_median(numbers):
    numbers.sort()
    middle_index = len(numbers) // 2
    if len(numbers) % 2 != 0:
        return numbers[middle_index]
    # return (numbers[middle_index] + numbers[middle_index - 1]) / 2
my_numbers = [4, 2, 8, 5, 9, 6, 3, 7, 1]
median_value = calculate_median(my_numbers)
print("The median value is:", median_value)

# Write a Python program that takes a list of numbers as input and outputs the second largest number in the list using conditional statements and a for loop.
numbers = [4, 8, 2, 10, 15, 13, 9]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num

print("The second largest number in the list is:", second_largest)


# Write a Python program that takes a year as input and determines if it is a leap year.
year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# Write a Python program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards),
#  ignoring spaces and punctuation.
#Using lists and reverse() method
def isPalindrome(s):
    x=list(s)
    y=[]
    y.extend(x)
    x.reverse()
    if(x==y):
        return True
    return False
  
s ="teacher"
ans = isPalindrome(s)
  
if ans:
    print("Yes")
  
else:
    print("No")