# Read file
f = open("E:/Python_Tutorial/Basics/files/Demo.txt", "r")
content = f.read()
print("Reading File Content:\n", content)
f.close()

# # Write to file
f = open("E:/Python_Tutorial/Basics/files/Demo.txt", "w")
chars_written = f.write("Hi partner")  # Overwriting content
print(f"\nWriting to File:\n{chars_written} characters written.")
f.close()

# # # Append to file
f = open("E:/Python_Tutorial/Basics/files/Demo.txt", "a")
chars_appended = f.write("\nHow are you?")  # Appending new content
print(f"\nAppending to File:\n{chars_appended} characters appended.")
f.close()


# # reading line by line
f = open("E:/Python_Tutorial/Basics/files/Demo.txt", "r")
for line in f:
    print(line.strip())
f.close()


# # another method using with open 
with open("E:/Python_Tutorial/Basics/files/Demo.txt", "r") as f:
    print(f.read())
    
# # create file(x):The x mode is used to create a new file. It raises an error if the file already exists.


try:
    f = open("E:/Python_Tutorial/Basics/files/NewDemo.txt", "x")
    f.write("This file is created using 'x' mode.")
    f.close()
except FileExistsError:
    print("File already exists.")
    
# # r+ mode allow to read and write t a file 

try:
    f= open("E:/Python_Tutorial/Basic/files/Demo.txt","r+")
    print("before writing:\n",f.read())
    f.write("\nThis is adding using 'r+' mode.")
    f.seek(0) #move cursour to the beginning
    print("after write:\n",f.read())
    f.close()
except FileNotFoundError:
    print("File not found")    
    

# #w+ mode allow to read and write but it overwrite th file if it existss or create a new file 
f = open("E:/Python_Tutorial/Basics/files/NewDemo.txt", "w+")
f.write("this is content is written using 'w+' mode .\n")
f.seek(0)
print(f.read())
f.close()

# # The a+ mode allows you to read and append. It creates a new file if it doesn't exist.

f = open("E:/Python_Tutorial/Basics/files/Demo.txt", "a+")
f.write("\nThis is appended using 'a+' mode.")
f.seek(0)  # Move cursor to the beginning
print(f.read())
f.close()


# # summary
# # x	Create a new file, error if it exists.
# # r+	Read and write, file must exist.
# # w+	Read and write, overwrite existing file.
# # a+	Read and append, create file if missing.
    
    
    
    
# # for json file
import json

data={
    "name":"Varsani",
    "age":10,
    "skills":["python","Java"]
}
# writing to json file
with open("E:/Python_Tutorial/Basics/files/data.json", "w") as json_file:
  json.dump(data,json_file)  #dump means serialize python obj to json file
  
# # reading from a json file
with open("E:/Python_Tutorial/Basics/files/data.json", "r") as json_file:
    data = json.load(json_file)
    print("Data read from JSON file:")
    print(data)
    
    
# # checking if json file exists    # 
import os

file_path = "E:/Python_Tutorial/Basics/files/data.json"

if os.path.exists(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        print("JSON file exists and was read successfully.")
else:
    print("JSON file does not exist.")
