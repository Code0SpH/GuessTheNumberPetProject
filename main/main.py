import random

random_number = random.randint(1, 100)
counter_attempts = 0

while True:
    guess = int(input("Угадайте число от 1 до 100: "))
    counter_attempts += 1
    if guess < random_number:
        print("Слишком мало!")
    elif guess > random_number:
        print("Слишком много!")
    else:
        print(f"Поздравляем! Количество попыток -  {counter_attempts}")
        break