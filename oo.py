#open file and read its contents
file  = open('coo.txt','r')
#print(file.read())
file.close()

#open file and read its beginning 8 characters
file = open('coo.txt','r')
print("\n Read in parts \n")
print(file.read(9))
file.close()

#append your name and age in the file
file = open('coo.txt','a')
file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()

# open the fille in write mode
file_write = open('coo.txt','w')
#write in the file
file_write.write("File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr. old")
file_write.close()