# What is file handling?
# 1.Opening a file
# Example No.01
file = open("example.txt","r")
print(file.read())
file.close
# Example No.02
file = open("example.txt","w")
file.write("Hello, world!")
file.close
# Example No.03
file = open("example.txt","a")
file.write("Hello, world!")
file.close
# Example No.04
file = open("example.txt","r")
print(file.read())
file.close
# Example No.05
file = open("example.txt","r")
print(file.read())
file.close
# Reading a file
# Example No.01
content = file.read()
print(content)
file.close()
# Example No.02
suffer = open("subway.txt","r")
content = subway.read()
print(content)
suffer.close
# Example No.03
subway = open("subway.txt","r")
content = subway.read()
print(content)
subway.close
# Example No.04
subway = open("subway.txt","r")
content = subway.read()
print(content)
subway.close
# Example No.05
subway = open("subway.txt","r")
content = subway.read()
print(content)
subway.close
# Writing a file
# Example No.01
file = open("example.txt","w")
file.write("Hello, world!")
file.close()
# Example No.02
file = open("example.txt","w")
file.write("Subway is the best!")
file.close()
# Example No.03
file = open("example.txt","w")
file.write("Integration is the best!")
file.close()
# Example No.04
file = open("example.txt","w")
file.write("Call of duty")
file.close()
# Example No.05
file = open("example.txt","w")
file.write("Sub-Engineer")
file.close()
# Appened data
# Example No.01
file = open("example.txt","a")
file.write("Hello, world!")
file.close()
# Example No.02
file = open("example.txt","b")
file.write("Subway is the best!")
file.close()
# Example No.03
file = open("example.txt","c")
file.write("Integration is the best!")
file.close()
# Example No.04
file = open("example.txt","d")
file.write("Call of duty")
file.close()
# Example No.05
file = open("example.txt","e")
file.write("Sub-Engineer")
file.close()

# Different file methods
# Example No.01
with open("example.txt","r") as f:
    print(f.read())
    f.seek(0)
    print(f.read())
    f.seek(0)
    print(f.readline())
    
# Example No.02
with open("example.txt","r") as f:
    print(f.read())
    f.seek(2)
    print(f.read())
    f.seek(3)
    print(f.readline())
    
# Example No.03
with open("example.txt","r") as f:
    print(f.read())
    f.seek(0)
    print(f.read())
    f.seek(0)
    print(f.readline())
    
# Example No.04
with open("example.txt","r") as f:
    print(f.read())
    f.seek(0)
    print(f.read())
    f.seek(0)
    print(f.readline())
    
# Example No.05
with open("example.txt","r") as f:
    print(f.read())
    f.seek(0)
    print(f.read())
    f.seek(0)
    print(f.readline())
    
# with statemtent
# Example No.01
with open("mixture.txt","r") as f:
    print(f.read())
    
# Example No.02
with open("mixture.txt","r") as f:
    print(f.read())
    
# Example No.03
with open("mixture.txt","r") as f:
    print(f.read())
    
# Example No.04
with open("mixture.txt","r") as f:
    print(f.read())
    
# Example No.05
with open("mixture.txt","r") as f:
    print(f.read())
    
# Iterate through a file
# Example No.01
with open("mixture.txt","r") as f:
    for line in f:
        print(line)
        
# Example No.02
with open("mixture.txt","r") as f:
    for line in f:
        print(line)
        
# Example No.03
with open("guru.txt","r") as f:
    for line in f:
        print(line)
        
# Example No.04
with open("dead.txt","r") as f:
    for line in f:
        print(line)
        
# Example No.05
with open("space.txt","r") as f:
    for line in f:
        print(line)
        
# Example No.06
with open("space.txt","r") as f:
    for line in f:
        print(line)
    
    

