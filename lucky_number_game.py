import random

def play_game():
    lucky_number = random.randint(1, 50)
    attempts = 0

    print("🎮 Lucky Number Game")
    print("1 se 50 ke beech number guess karo!")

    while True:
        try:
            user_number = int(input("Enter your number: "))
            attempts += 1

            if user_number == lucky_number:
                print("🎉 Congratulations! You guessed the lucky number!")
                print("Attempts:", attempts)
                break

            elif user_number < lucky_number:
                print("⬆️ Thoda bada number try karo.")

            else:
                print("⬇️ Thoda chhota number try karo.")

        except ValueError:
            print("❌ Please sirf number enter karo.")


play_game()