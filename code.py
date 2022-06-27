#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[18]:


import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
    
)

print(mydb)
mycursor = mydb.cursor(buffered=True)


# In[3]:


mycur


# In[5]:


mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)


# In[22]:


mycursor.execute("DROP DATABASE schooldataBase")             


# In[23]:


mycursor.execute("CREATE DATABASE schooldataBase")


# In[30]:



import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
    
)

cursorObject=mydb.cursor()

#mycursor.execute
Student_details=("CREATE TABLE Student_details(id INT(8) ZEROFILL ,name VARCHAR(10), adhar_card_no INT(12) ,Parent_name VARCHAR(10), Phone_number INT(10),class INT(4), section CHAR(2))")
cursorObject.execute(Student_details)
mydb.close()


# In[1]:


import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
    
)

cursorObject=mydb.cursor()

Student_details=("INSERT INTO 'student_details' (`id`, `name`, `adhar_card_no`, `Parent_name`, `Phone_number`, `class`, `section`) VALUES ('1022003', 'Mani Reddy', '9014', 'Harsha', '909898096', '8', 'A')")
cursorObject.execute(Student_details)
mydb.close()


# In[2]:


import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
    
)

cursorObject=mydb.cursor()

Student_details=("delete from student_details where id = 01022002")
cursorObject.execute(Student_details)
mydb.close()


# In[4]:


import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
    
)

cursorObject=mydb.cursor()

Student_details=("INSERT INTO `student_details` (`id`, `name`, `adhar_card_no`, `Parent_name`, `Phone_number`, `class`, `section`) VALUES ('1022004', 'Rakesh', '9013', 'Suresh', '909898097', '8', 'A')")
cursorObject.execute(Student_details)
mydb.close()


# In[6]:



import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
    
)

cursorObject=mydb.cursor()

#mycursor.execute
Student_marks=("CREATE TABLE Student_marks AS (id INT(8) ZEROFILL ,Sub_id INT(10) ,Quarterly INT(10) ,Half_yearly INT(10) ,Annual INT(10))")
cursorObject.execute(Student_details)
mydb.close()


# In[7]:



import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
    
)

cursorObject=mydb.cursor()

#mycursor.execute
Student_marks=("CREATE TABLE Student_marks (id INT(8) ZEROFILL ,Sub_id INT(10) ,Quarterly INT(10) ,Half_yearly INT(10) ,Annual INT(10))")
cursorObject.execute(Student_marks)
mydb.close()


# In[8]:



import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
    
)

cursorObject=mydb.cursor()

#mycursor.execute
Subjects=("CREATE TABLE Subjects (sub_name VARCHAR(20) , sub_id INT(8)")
cursorObject.execute(Subjects)
mydb.close()


# In[14]:


import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
)

cursorObject=mydb.cursor()

#mycursor.execute
Subjects=("CREATE TABLE Subjects (subject_name VARCHAR(20) ,subject_id INT(8))")
cursorObject.execute(Subjects)
mydb.close()


# In[17]:


import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
)

cursorObject=mydb.cursor()

#mycursor.execute
Subjects=("INSERT INTO subjects VALUES ('Social',003)")
cursorObject.execute(Subjects)
mydb.close()


# In[18]:


import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
)

cursorObject=mydb.cursor()

#mycursor.execute
Subjects=("INSERT INTO subjects VALUES ('Science',002)")
cursorObject.execute(Subjects)
mydb.close()


# In[19]:


import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
)

cursorObject=mydb.cursor()

#mycursor.execute
Subjects=("INSERT INTO subjects VALUES ('Science',002)")
cursorObject.execute(Subjects)
mydb.close()


# In[25]:



import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='schooldatabase'
   
    
)

cursorObject=mydb.cursor()

#mycursor.execute

Student_marks=("INSERT INTO `student_marks` (`id`, `subject_id`, `Quarterly`, `Half_yearly`, `Annual`) VALUES ('1022001', '001', '78', '82', '88')")
cursorObject.execute(Student_marks)
mydb.close()


# In[26]:


import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="ADMIN",
   password="Admin",
   database='schooldatabase'
   
    
)

print(mydb)
mycursor = mydb.cursor(buffered=True)


# In[27]:


import mysql.connector


mydb = mysql.connector.connect(
   host="localhost",
   user="Teacher",
   password="Teacher",
   database='schooldatabase'
   
    
)

print(mydb)
mycursor = mydb.cursor(buffered=True)


# In[ ]:




