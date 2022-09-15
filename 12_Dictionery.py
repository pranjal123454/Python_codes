# myDict={
#     "fast":"In a quick manner",
#     "Harry":"A Coder",
#     "Marks":[1,2,5],
#     "anotherdict":{'harry':'player'}

# }
# print(myDict['fast']) key value deta hn
# print(myDict['Marks'])
# print(myDict['anotherdict']['harry'])  dictionery mein dictioney rkh sakte hn
# #It is unordered
# #it is muttable
#  we can change it


#dict methods
myDict={
    "fast":"In a quick manner",
    "Harry":"A Coder",
    "Marks":[1,2,5],
    "anotherdict":{'harry':'player'}

}
print(myDict.keys())   #keys dega yh
print(myDict.values())
print(myDict.items())
updateDict={              #update aese krenge 
    "lovish":"A singe"
}
myDict.update(updateDict)
print(myDict)
myDict.get(["harry"])   #  if dict mein ni hn to null dega lekin myDict(['Harry']) krenge to error dega
