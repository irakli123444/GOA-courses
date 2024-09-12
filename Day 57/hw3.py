def number():
    sum = 0

    number_list = [499, 9278, 28, 9, 90, 992,]
    for i in range (len(number_list)): 
        sum = sum + number_list[i]

    print(sum / len(number_list))

number()    