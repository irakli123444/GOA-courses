def number():
    user1 = int(input("enter a number: "))
    user2 = int(input("enter a number: "))
    if user1 > user2:
        return user2
    elif user2 > user1:
        return user1
    elif user1 == user2:
        return "ნეიტრალი"
print(number())
    

