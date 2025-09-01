import random
from typing import TypedDict

class GuessInfo(TypedDict): # so the type checker won't complain
    isPerfect: bool
    result_letters: list[str]

words = ["other", "first", "click", "price", "state", "world", "music", "video", "order", "group", "under", "hotel", "store", "local", "phone", "board", "moral", "mayor", "prime", "watch", "power", "peace", "point", "limit", "pound", "thank", "think", "value", "valid", "wheel", "water", "solve", "force", "smart", "focus", "sugar", "radio", "voice", "throw", "magic", "major", "sight", "judge", "earth", "media", "green", "grass", "drama", "image", "dozen"]
# 50 words

"""
displays the wordle grid in the format
_____________________
| 1 | 2 | 3 | 4 | 5 |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
def display_grid(letters: list[str], attempts: int) -> None:
    print("_____________________")
    print(f"| {letters[0]} | {letters[1]} | {letters[2]} | {letters[3]} | {letters[4]} |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print(f"Attempt: {attempts}/5")

def choose_word(choices: list[str]) -> str:
    return random.choice(choices)

# if letter is in word and in correct place, wrap the letter with ⸨⸩, if letter is in word but not in correct place, wrap with [], else if not in word, wrap with --
def check_guess(user_guess: str, solution: str) -> GuessInfo:
    correct_letters: int = 0
    guess_info: GuessInfo = {
        "isPerfect": False,
        "result_letters": [], # 5 spaces for 5 letters 
    }

    #"""
    print(f"user_guess: {user_guess}")
    print(f"solution: {solution}")
    #"""

    for i, letter in enumerate(user_guess): # enumerate() returns pair of (index, value) while looping
        if letter in solution:
            if letter == solution[i]:
                guess_info["result_letters"].append(f"⸨{user_guess[i]}⸩")
                correct_letters += 1
            else:
                guess_info["result_letters"].append(f"[{user_guess[i]}]")
        else:
            guess_info["result_letters"].append(f"-{user_guess[i]}-")
    if correct_letters == 5:
        guess_info["isPerfect"] = True
    
    return guess_info

def main() -> None:
    can_guess: bool = True
    attempts: int = 0
    solution: str = choose_word(words)
    print("--------- WORDLE ULTRALITE ---------")
    while can_guess:
        if attempts < 5:
            user_guess: str = input("Guess: ")
            attempts += 1
            guess_info: GuessInfo = check_guess(user_guess, solution)
            display_grid(guess_info["result_letters"], attempts)
        else:
            # end game - fail
            play_again: str = input("Sorry, you ran out of guesses! Would you like to play again? (Y/N)")
            if play_again.upper() == "Y":
                attempts = 0
                solution = choose_word(words)
            else:
                can_guess = False

        # end game - success
        if guess_info["isPerfect"]:
            print("Congratulations for guessing the word!")
            play_again: str = input("Would you like to play another round? (Y/N)")
            if play_again.upper() == "Y":
                solution = choose_word(words)
            else:
                print("Thanks for playing!")
                can_guess = False


if __name__ == "__main__":
    main()