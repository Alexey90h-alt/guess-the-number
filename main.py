import random

def game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("🎯 Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        user_input = input("Введи число (или 'выход'): ")

        if user_input.lower() == 'выход':
            print("Жаль, что ты уходишь. Приходи еще!")
            break

        # Проверка: ввел ли пользователь число
        if not user_input.isdigit():
            print("❌ Ошибка! Нужно ввести целое число.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < number_to_guess:
            print("📈 Больше!")
        elif guess > number_to_guess:
            print("📉 Меньше!")
        else:
            print(f"🎉 ПОЗДРАВЛЯЮ! Ты угадал число за {attempts} попыток!")
            break

if __name__ == "__main__":
    game()