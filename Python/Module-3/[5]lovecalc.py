# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name=name1+name2
name=name.upper()
T=name.count('T')
R=name.count('R')
U=name.count('U')
E=name.count('E')
L=name.count('L')
O=name.count('O')
V=name.count('V')
E=name.count('E')
l=str(T+R+U+E)
r=str(L+O+V+E)
sum1=int(l+r)
if sum1<=10 or sum1>=90 :
    print("Your score is ",sum1,", you go together like coke and mentos",sep=(''))
elif 40<=sum1<=50 :
    print("Your score is ",sum1,", you are alright together.",sep=(''))
else :
    print("Your score is",sum1)
