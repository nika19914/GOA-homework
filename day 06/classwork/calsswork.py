
#1) მოხარებელს შეეკითხეთ მისი სახელი,გვარი ასაკი და იმეილი, შემდეგ კი შემოტანილი მნიშვნელობები დაბეჭდეთ ტერმინალში. გამოიყენეთ ეტიკეტი, რომ მიანიშნოთ მომხარებელს თუ რა უნდა შემოიტანოს კონკრეტულ შესაყვან ველში.


#

#3) კომენტარებით ახსენით თუ რა არის input და output, ასევე რისთვის გამოიყენება ისინი

#input- ვიყენებთ იმისთის რომ გავიგოთ და შემოვიტანოთ ან მომხმარებლის რაიმე ინფორმაცია 

num01=int(input("enter first number: "))
num02=int(input("enter second number: "))
chose_number=int(input("chose any action like, +, -, *, /: "))

print("A") if num01 > num02 else print("=") if num01 == num02 else print("B")
