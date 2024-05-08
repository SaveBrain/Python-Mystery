# ApnaCollege      
'''i = 1
while i <= 5:
    print(i)
    i += 1
print(i)'''


# Q1 : print numbers from 1 to 100
'''i = 1 
while i <= 100:
    print(i)
    i += 1'''
    

# Q2 : print the numbers from 100 to 1
'''i = 100
while i >= 1:     # this is a stopping condition
    print(i)
    i -= 1'''
    
    
# Q3: print the multiplication table of a number n
'''n = int(input("Enter Your Number : "))
i = 1

while i <= 10:
    print(n*i)
    i += 1'''


# Q4: print the elements of the following list using loop : 
# [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]
'''nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0 # index alawys start with 0
while idx < len(nums):
    print(nums[idx])
    idx += 1'''



# search for a number x in this tuple using the loop 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter Your Digit : "))

i = 0
while i < len(nums):
    if (nums[i]==x):
        print("found at index", i)
    else:
        print("finding")
    i += 1'''



# For loop

# print the elements of the following list using a loop 
# [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]
'''nums = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]

for i in nums:
    print(i)'''
    


# search for a number x in this tuple using the loop 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
'''nums = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49 )

x = 49

idx = 0

for el in nums:
    if (el == x):
        print("found the number at index", idx)
        break
    idx += 1'''



# Even number
'''for i in range(2, 101, 2):
    print(i)'''
    
    
    
# Odd number
'''for i in range(1, 100, 2):
    print(i)'''
    
    

# Using for & range()

# print numbers from 1 to 100
'''for i in range(1, 101):
    print(i)'''
    


# print numbers from 100 to 1 
'''for i in range(100, 0, -1):
    print(i)'''
    
    
    
# print the multiplication table of a number n
'''n = int(input("Enter your number : "))

for i in range(1, 11):
    print(n*i)'''
    
    
# pass er mane hocche loop er moddhe kono kaj korabo nah 
'''for i in range(5):
    pass
print("lol")'''



# WAP to find the sum of first n numbers. (using for)
'''n = 5 
sum = 0

for i in range(1, n+1):
    sum += i

print("total sum = ", sum)'''



# WAP to find the sum of first n numbers. (using while)
'''n = 5
sum = 0

i = 1
while i <= n:
    sum += i 
    i += 1
print("total sum =", sum)'''



# WAP to find the factorial of the first n numbers. (Using while) 
'''n = 5
fact = 1

i = 1
while i <= n:
    fact *= i 
    i += 1
print("factorial =", fact)'''




# WAP to find the factorial of the first n numbers. (Using for) 
n = 5
fact = 1

for i in range(1, n+1):
    fact *= i
    
print("factorial =", fact)