#Write a program to create a list of fruits and copy only 'e' letter fruits to the new list

fruits = ["apple", "banana", "cherry", "kiwi", "mango","greenappe","avacado"]
newlist = []

for x in fruits:
  if "e" in x:
    newlist.append(x)

print(newlist)


#write Pgm to find prime number or not
num = int (input("enter a number"))
for i in range(2,num):
  if num%i==0:

    print('Not Prime')
    break
else:
  print("Prime")
