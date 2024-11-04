#გააკეთეთ პრეზენტაცია ინტერნეტზე(როგორ მუშაობს ის და როგორ უკავშირდება ერთი კომპიუტერი მეორეს)

#2) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხვი


#numbers = [23, 56, 99, 8123, 244, 75]


#largest_number = numbers[0]  


#for number in numbers:
    #if number > largest_number:
        #largest_number = number


#print( largest_number)


#3) შექმენით რიცხვების სია და დაბეჭდეს სიის თითოეული რიცხვის ფაქტორიალ
#numbers = [5, 7, 3, 2, 6]

#for number in numbers:
    #product = 1

    #for i in range(1, number + 1):
        # product = product * i
        #product *= i
    
    #3print(product)

#4) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხვი


#numbers = [23, 576, 69, 871, 470, 785]


#smaller_number = numbers[0]  

#for number in numbers:
    #if number < smaller_number:
        #smaller_number = number


#print( smaller_number)


#5) შექმენით რიცხვების სია სადაც გექნებათ დადებითი და უარყოფითი რიცხვები, შემდეგ შექმენით ახალი სია სადაც გექნებათ მხოლოდ უარყოფითი რიცხვები და დაბეჭდეთ ის(გამოიყენეთ while).

#numbers = [5, -7, 3, 2, -11, 6, 8, -10, 12, 15, -17, 19, -21]

##negative_numbers = []

#index = 0

#while index < len(numbers):
    #if numbers[index] < 0:
        #negative_numbers.append(numbers[index])
    #index += 1

#print(negative_numbers)




#6) შექმენით რიცხვების სია და დაპრინტეთ სიის თითოეული ელემენტი უკუღმა(გამოიყენეთ range() ფუქნცია ან შექმენით ცვლადი
# chars = ["a", "a", "a", "b", "c", "b", "c"]

# no_duplicates = []

# for char in chars:
#     if no_duplicates.count(char) == 0:
#         no_duplicates.append(char)

# chars = ["a", "a", "a", "b", "c", "b", "c"]

# no_duplicates = []

# for char in chars:
#     if char not in no_duplicates:
#         no_duplicates.append(char)

# print(no_duplicates) 




#7) შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება
#simbols=[ "%", "/", "*", "<", ">","%", "/", "*", "<", ">"]
#simbols_1=["%", "/", "*", "<", ">"]

#8) შექმენით ცლვადი სადაც შეინახავთ string-ს, შემდეგ შექმენით ახალი ცვლადი სადაც შეინახავთ ამ სტრინგს შემოტრიალებულად და დაბეჭდეთ ის


#names= ( "sandro", "givi", "anna", "ikuna", "alexander", "rezi", "aleko", "nika", "otto")
#names_1=("otto", "nika", "aleko", "rezi", "alexander", "ikuna", "anna", "givi", "sandro" )

#print(names_1)


#9) დაწერეთ პროგრამა, რომელიც მომხამრებელს შემოატანინებს რიცხვს და აბრუნებს სიას, სადაც იქნება გამდოცემული რიცხვის ყველა გამყოფი
#years = int(input("Enter the number of years: "))

#century = years // 100
#remaining_years = years % 100

#if remaining_years == 0:
    #print(century)
#else:
    #print(century + 1)

#10) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და დაპრინტავს რომელი საუკუნეა ის




