#``` 1 ) შექმენით რიცხვებით სავსე სია და დაბეჭდეთ სიის ელემენტების საშუალო არითმეტიკული ```
sum = 0

number_list = [1, 3, 5, 7, 10, 12 ]
for i in range (len(number_list)): 
    sum = sum + number_list[i]

print(sum / len(number_list))