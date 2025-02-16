#read first line of file
file = open('coo.txt','r')
print("Reading first line...")
print(file.readline())
print(file.readline())
print(file.readlines())
file.close()
