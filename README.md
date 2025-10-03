# What is file handling?
File handling in python refers to the ability to create, open, read, write, and close files (like text files, CSVs,etc) using built in functions and methods. It’s an essential part of programming for tasks like data processing, logging, and configuration management.

# Basic of file handling in python
The basics of file handling in python involve a few key concepts and operations that allow you to work with files, -creating, reading, and closing them.
print

## 1.Open a file in python
To work with files in python, the first step is to open the file using the built –in open () function.

**Syntax**

												file = open (“filename”, “mode”)

## 2.Reading a file
Once you’ve opened a file using open (), you can read its contents using several built in method.
Read entire content of the file as a single string.

## 3.Writing data
To write data to a file, you use the open () function with modes like:
-	‘W’ –write(overwrites existing content)
-	  ‘a’ –appened(adds to the end of the file)
-	   ‘X’ –Exclusive creation(fails if the files exists)
-	   
## 4.Appened data 

Appending means adding data to the end of a file without deleting the existing content.
You do this by opening the file in append mode.

**Syntax**

											with open(“filename.txt”, “a”) as file:
											  file.write(“Your new data here\n”)
											
## 5.Different file modes
When working with files in python using the open() function, the file mode tells python how to open the file:  for reading, writing, appending, etc.

## 6.File methods
Once you open the file using open() function, python provides various file methods to interact with it –like reading, writing, checking position, etc.
Some common methods are given below

-	Seek()
-	Read()
-	Readline()
-	Readlines()
-	Write()
-	Writelines()
  
## 7.With statement
The with statement in python is used for resource management –especially when working with files. It automatically handles opening and closing the file, even if an error occurs.

-	You have to manually ensure the file is closed using file. Close (), even if an error happens.
-	The file is automatically closed when the block inside with is finished.
-	Cleaner and less error –prone.
-	No need for try –finally blocks.
-	
## 8.Iterate through a file
When reading large files or processing data line –by –line (e.g., CSVs), it’s efficient to iterate over the file object directly.

**Example: **

				With open(“example.txt”,”r”) as file:
					Lines = filereadlines ()
					      for line in lines:
					     print(line.strip ())














