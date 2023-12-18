# write a program to odd or even number in using conditional oprater

num1=int(input("enter a number"))
if num1%2==0:
  print(num1,("number is odd"))
else:
  print(num1,("number is even"))


# find the largest number of three

n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the third number"))
if n1>n2 and n1>n3:
  print(n1,("number is largest"))
elif n2>n3 and n2>n1:
  print(n2,("number is largest"))
else:
  print(n3,("nummber is largest"))

#find leap year using conditional statement

year=int(input("enter the year"))
if year%4==0:
  print(year,("year is leap year"))
else:
  print(year,("is not a leap year"))


#find summing numbers using while loop

number=int(input("enter a number: "))
i=1
sum=0
while(i<=number):
    sum=sum+i
    i=i+1
print(sum,("suming of the"),number)

#⁠find countdown of a number using while loop
count=int(input("enter the  number for count"))
i=1
value=0
while(i<=count):
  count-=1
  print(count)

