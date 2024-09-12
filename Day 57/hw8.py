def time():
    question1 = int(input("რამდენი წლის ხარ: "))
    question2 = int(input("რომელი წელია ეხლა: "))
    question3 = input("წარსულში გინდა რომ გადაინაცვლო თუ მომავალში: ")
    question4 = int(input("რამდენი ხნით გინდა რომ გადაინაცვლო: "))
    if question4 == "წარსული":
        print("თქვენ გადაინაცვლეთ წარსულში")

    if question4 == "მომავალი":
        print("თქვენ გადაინაცვლეთ მომავალში")
    
    
    print("თქვენ გადაინაცვლეთ question4 წლით")
    
    print("თქვენ ხართ ")
    if question4 == "წარსული":
        print("question1 - question4 წლის")

    if question4 == "მომავალი":
        print("question1 + question4 წლის")
    
    
