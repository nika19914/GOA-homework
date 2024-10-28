#პაროლის ვალიდაციის პროგრამა:
#შექმენით ცვლადი სადაც შეინახავთ პაროლს(მაგალითად: goa1234)


secret_pass = "luka1234"
user_pass = ''

tries = 3

while tries > 0 and user_pass != secret_pass:
    user_pass = input("Enter your password (you have " + str(tries) + " tries left): ")
    tries = tries - 1

    if user_pass == secret_pass:
        print("Access granted!")
    elif tries == 0:
        print("You've reached the maximum number of tries. Access denied!")
    else:
        print("Access denied! Try again.")





# secret_num = 7
# user_num = 0

# while user_num != secret_num:
#     user_num = int(input("Guess the number: "))

#     if user_num > secret_num:
#         print("Your number is too high!")
#     elif user_num < secret_num:
#         print("Your number is too low!")
#     else:
#         print("Congratulations! You guessed the correct number.")
