#List Comprehension
StudentNames=["Ashvatha","Logeswari","Saisanghavi","MahaVishnu","Subasri","Abirami"]
NewStudentNames=[]
for item in StudentNames:
    if (item!="Abirami"):
        NewStudentNames.append(item)
print("The List of New Student Names are:",NewStudentNames)