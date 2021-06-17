#!/usr/bin/env python
# coding: utf-8

# # STUDENT INFORMATION SYSTEM

# ![Screenshot%20%2822%29.png](attachment:Screenshot%20%2822%29.png)

# CONCEPTS USED

# - 1.DICTIONARIES
# - 2.LOOPS
# - 3.CONDITIONAL STATEMENTS
# - 4.INPUT()
# - 5.PRINT()
# - 6.LISTS
# 

# Code

# In[ ]:


M={}#This is the master dictionary which gonna save all the information given by user and while perorming specific tasks this information is used. 


# In[ ]:


A='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
degree=['CS','CE','EE','CH','BT','MT','ME','EC','TT','PH','HR',]
n=0
print('Welcome to the information system')
U=input('choose tasks to peform from 1 to 6 - ')
if U=='1':
    print('Enrolling a new student. Enter the following details')
    for x in range(0,100):
        a=input('Name : ')
        for i in a:
            if i in A:
                n+=1
            else:
                print('enter only alphabet')
        if n==len(a):
                break
    for x in range(100):
        b=input('DOB  (yyyy-mm-dd): ')
        if ((1980<int(b.split('-')[0])<2005) and 0<int(b.split('-')[1])<13 and 0<int(b.split('-')[2])<32):
            break
        else:
            print('enter a valid DOB')
    c=input('Address  : ')
    for x in range(100):
        d=float(input('class X percentage  : '))
        if 0<d<100:
            break
        else:
            print('enter a valid percentage(0-100)  ')
    for x in range(100):
        e=float(input('Class XII percentage : '))
        if 0<e<100:
            break
        else:
            print('enter a valid percentage (0-100) ')
    for x in range(100):
        f=input('Current Year  : ')
        if 0<int(f)<6:
            break
        else:
            print('enter a valid year (1-5) ')
    while True:
        g=str(input('Degree:'))
        if g not in degree:
            print('enter a valid degree from ',d)
        else:
            break
    for x in range(100):
        h=input('GPA  : ')
        if 0<=float(h)<=10:
            break
        else:
            print('enter a valid GPA (0-10)')
    M[a]={}
    M[a]['Name']=a
    M[a]['DOB']=b
    M[a]['Address:']=c
    M[a]['Class X percentage']=d
    M[a]['Class XII percentage']=e
    M[a]['Current Year']=f
    M[a]['Degrees']=g
    M[a]['GPA']=h
if U=='2':
    print('Updating a student detail')
    u1=input('enter the student name whose details are to be updated  :      ')
    u2=input('enter the detail which has to be updated  :  ')
    u3=input('enter updated value or detail  :  ')
    M[u1][u2]=u3
if U=='3':
    print("Deleting a student's details ")
    r1=input('enter the student name whose details you want to delete  :  ')
    del M[r1]
if U=='4':
    print('Sorted list of students based on their names and sorted list of students based on their GPA ')
    L4=[]
    a4=sorted(M.keys())
    for i in a4:
        print(i)
    print('\n','_______________\n')
    list=[]
    for i in M.keys():
        list.append(float((M[i]['GPA'])))
    Z=sorted(list,reverse=True)
    for i in Z:
        for j in M.keys():
            if float(M[j]['GPA'])==i:
                print(j,'with GPA= ',i)
if U=='5':
    print('Students with GPA in between the given range  ')
    a1=float(input('lower limit of range '))
    a2=float(input('upper limit of range'))
    list1=[]
    for i in M.keys():
        if a2>float(M[i]['GPA'])>a1:
            list1.append(float((M[i]['GPA'])))
    Z=sorted(list1,reverse=True)
    for i in Z:
        for j in M.keys():
            if float(M[j]['GPA'])==i:
                print(j )
if U=='6':
    list=[]
    for i in M.keys():
        list.append(float((M[i]['GPA'])))
    Z=sorted(list,reverse=True)
    print('top 5 performers in each degree')
    print('\n')
    for z in degree:
        print('top 5 performers in ',z)
        D=[]
        for i in M.keys():
            if M[i]['Degrees']==z:
                D.append(M[i]['Name'])
        for i in Z:
            no=0
            for j in D:
                if float(M[j]['GPA'])==i:
                    print(j,'with GPA= ',i)
                    no=no+1
                if no==5:
                    break
        print(end='\n')
        
        
            
            
            
            
    
    
    
    


# In[ ]:


M


# Instructions to run the program

# - 1)Define M. Run the program
# - 2)The program asks you to select a numerical from 1-6
# - 3)Select a numerical based on the task you want to perform
# - 4)Based on the numerical you have selected the program performs speciic tasks and asks you for inputs if needed.
# - 5)You need to give valid inputs
# - 6)The program stops when the task you asked for is completed
# - 7)Everything is saved in the Dictionary M
# - 8)Each student's details are saved in a dictionary which is named after the student himself in M.
# - Note: In order to perform tasks you first need to input data by selecting 1 and enrolling all the students' data.initially M will be empty.

# In[ ]:




