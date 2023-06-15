

questions = [

{"question": "'Сколько минут в 1 часе ?",

"answers":['10','30','60'],

"right_answer": 3

},

{"question": "'Сколько дней в месяце в среднем ?",

"answers":['70','10','30'],

"right_answer": 3

},

{"question": "Сколько грамм в килограммах ?",

"answers":["1099","1000","900"],

"right_answer": 2

}

]

score = 0

for q in questions:

   print(q['question'])

   print(', '.join(q['answers']))

   user_answer = int(input("Введи вариант ответа: "))

   if user_answer == q['right_answer']:

       print("Верно, +1 очко")

       score += 1

   else:

       print("Не верно")        

print(f"Ваши очки: {score}")

if score>2:

   print("Ты победил")

else:

       print("Ты проиграл")