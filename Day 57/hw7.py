def math():
    user1 = int(input("enter a number: "))
    if user1 > 0:
        return "დადებითი"
    elif user1 < 0:
        return "უარყოფითი"
    elif user1 == 0:
        return "ნეიტრალი"

print(math())