txt=input("Enter the string to be checked:")
target_word=input("enter the target word:")
x=txt.split(" ")
j=0
index_pos=[]
for i in x:
    if i==target_word:
        index_pos.append(j)
    j=j+1
print(index_pos)
