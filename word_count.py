sentence=input("Enter the string").lower()
x =sentence.split(" ")
y=[]
for i in x:
 if y.count(i)==0:
  y.append(i)
  print(i.title(),"-",sentence.count(i))
