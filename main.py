print("Добро пожаловать в Викторину")
print("Ответье на вопросы")

score = 0

# answer 1
answer1 = input("Сколько будет 2 * 2?")
if answer1 == "4":
    print("Верно")
    score +=1
else:
    print("Неверно")
    
    #answer 2 
    answer2 = input("Какого цвета роза?") .lower()
    if answer2 == "красная" or answer2 == "розовая":
        print("Правильно")
        score += 1
    else:
        print("Неверно")
        
        # output result
        print("Векторина окончена! Ваш общий счет:{score} из 2.")
