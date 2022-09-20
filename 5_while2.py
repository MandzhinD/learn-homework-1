"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"How are you?": "Good, thanks!","What are you up to?": "Drinking coffee and reading"} 

def ask_user(questions_and_answers):
    
  while True:
    user_q = input ('Спроси что-нибудь: ')
    if user_q in questions_and_answers.keys():
      print (questions_and_answers.get(user_q))
      break
    else:
      print (0)
      

if __name__ == "__main__":
    ask_user(questions_and_answers)
