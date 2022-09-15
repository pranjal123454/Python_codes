#use open function to read the file
f=open("sample.txt",'r')
data=f.read()
print(data)
f.close()
#other methods to read the file
# f.readline  read first line after that on second call it read second line
