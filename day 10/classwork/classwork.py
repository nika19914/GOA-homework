#1)მომხარებელს შემოატანინეთ მისი ასაკაი, შეინახეთ ის ცვლადში და შეადარეთ. თუ ასაკი არის ლუზი დაბეჭდეთ თქვენი ასაკი არის ლუწი. სხვა შემთხვევაში: თქვენი ასაკი არის კენტი

#age=int(input("enter you age: "))
#age1=age

#if age % 2 == 0:
    #print("your age is even")
#else:
    #print("your age is odd")

#2)გამოიტანეთ 10-დან 50-ის ჩათვლით ყველა ლუწი რიცხვი. გამოიყენეთ for loop-ი



for num in range(0, 50 + 1):
    if num % 2 == 0:
        print(num)
 