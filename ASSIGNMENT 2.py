#Task 1: Check if a Number is Even or Odd

num=int(input('Enter a number: '))
if num % 2 == 0 :
    print( num," is an even number." )
else :
    print ( num," is an odd Number." )


#Task 2: Sum of Integers from 1 to 50 Using a Loop

sum=0
for num in range (1,51):
    sum += num
print(' The sum of numbers from 1 to 50 : \t ',sum)
