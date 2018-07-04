import random


def correct_number_wrong_position():
    original_list = list(range(10))
    random.shuffle(original_list)
    digits = (original_list[:3])
    print(digits)  # Note that this is the answer and can easily be commented out before launching the game. to prevent
    # copying

    while True:
        entry = input("Please enter a 3 digit number")
        guess_list = []  # this list keeps the numbers you've input
        c = 0

        if len(entry) != 3:  # this is to ensure 3 digits are input, not more, not less
            print("Please, its supposed to be a 3 digit number")
            continue

        try:
            int(entry) / 2  # this is to ensure it is an integer being input
            guesses = list(entry)
            for x in guesses:
                if int(x) in digits:  # clue for a present or correct digit
                    print(f"Good, {x} is present")
                    guess_list.append(int(x))
                else:
                    pass

            if len(guess_list) == 0:  # this is for the case in which none of the guessed digits are right
                print("Hmmm, bad luck, none is correct!")
                continue
            else:  # more clues incase of the right positions, or wrong ones
                for i in guess_list:
                    index_guesses = guesses.index(i)
                    index_digits = digits.index(i)
                    if index_digits == index_guesses:
                        print(f"{i} is in the right position")
                        c += 1
                    else:
                        print(f"{i} is in the wrong position")

            if c == 3:  # when you are done guessing correctly
                print(f"{entry} is the correct number")
                try_again = input("Do you want to play again: Type yes or no")
                if try_again == "yes":
                    correct_number_wrong_position()
                else:
                    print("Thanks for playing, Bye!!")
                    break
            else:
                continue
        except ValueError:  # going around the value error message
            print("Done")
            continue


correct_number_wrong_position()
