'''
# Task 1: Read a File and Handle Errors
try :
    with open('sample.txt.','r') as file1 :
        reading_file = file1.read()
    print(reading_file)
except FileNotFoundError :
    print("Error : The file 'sample.txt' was not found.")
'''
# Task 2: Write and Append Data to a File
user_input1=input('Enter text to write to the file :')
file1 = open('output.txt','w')
writing_file = file1.write(user_input1+'\n')
print('Data is successfully written in output.txt. ')
user_input2=input('Enter a additional tex to append :')
file1 = open('output.txt','a')
appending_file= file1.write(user_input2+'\n')
print('Data successfully appended.')
file1.close()
print('Final content of output.txt file :')
file1 = open('output.txt','r')
final_content=file1.read()
print(final_content)
file1.close()
