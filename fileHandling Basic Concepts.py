#read
#write
#create
#delete
#open a file
#reading a file
f=open("New Python/newfile.csv","r")


#properties and method in dictionary

print(f.readline())
print(f.read())
f.close()
f=open("New Python/newfile.csv","r")

#closing file is important

file=(f.read())
fileStringSrray = file.split(",")
print(fileStringSrray)

fileStringline=file[0].split(",")
print(fileStringline)
