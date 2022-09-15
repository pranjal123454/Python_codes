#Sets is the collection of non repetive item
# a={1,3,4,5,1}   repeat ni hota element
# print(type(a))
# a=set() #empty set
# a.add(2)
# a.add(3)
# a.add(4)
# a.add(5)
# a.add(6)
# print(a)

# # set ke andr list ko ni dal sakte vo hashable ni hn hashable means change ho rha hn to vo hashable ni hn dict or list no ho sakte tuple ho sakta hn
# print(len(a))
# a.remove(5)
# print(a.pop()) # koi bhi element to delete kr deta hn

#ques1
# hindi ke sbd ke english mein dictionary
myDict={
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Item"
}
print("your options are",myDict.keys())
a=input("Enter the Hindi Word")
print("The meaning of your word is",myDict[a]) #error na mile phir null aajaye koi key na milne pr isliye humne .get use kiya hn

