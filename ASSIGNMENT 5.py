'''
# Task 1: Create a Dictionary of Student Marks
user_input=input("Enter a student's name :")
marks={'Alice':85,'Mike':89,'Nick':96,"Jean":99,'Martha':97,'Robart':81}
if user_input in marks :
    mark = marks[user_input]
    print(f"{user_input}'s marks : {mark}" )
else :
    print('Student is not found.')
'''

# Task 2: Demonstrate List Slicing
list=[1,2,3,4,5,6,7,8,9,10]
print('Original List : ',list)
number= list[0:5]
print('Extracted first five element :',number)
number.reverse()
print('Reversed extracted element : ', number)     