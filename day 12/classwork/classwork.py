#1) მომხარებელს შემოატანინეთ ორი რიცხვი, აიყვანეთ ისინი მე-3 ხარისხში და გაიგეთ მათი ჯამი, თუ ჯამი ლუწია დაპრინტეთ "Result is Even", სხვა შემთვევაში "Result is Odd"


# პირველი მომხმარებელს შემოვატანინოთ რაიმე ციფრი ინფუთის საშუალებით

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
#აგვყავს 3–ის ხარისხში
quality1=num1 ** 3
quality2=num2 ** 3 
#გავიგოტ არის თუ არა ლუწი ან კენტი
sum=quality1 + quality2
#ვიყენებთ ის ელს
if sum % 2 == 0:
    print("number is even")
else:
    print("odd")