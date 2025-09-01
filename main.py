import random
from typing import TypedDict

class GuessInfo(TypedDict):
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

# extract list from value assigned to result_letters from dict guess_info
def extract_guess_letters(guess_info: GuessInfo) -> list[str]:
    return guess_info["result_letters"]

def main() -> None:
    attempts: int = 0
    playing: bool = attempts < 5
    print("--------- WORDLE ULTRALITE ---------")
    while playing:
        solution: str = choose_word(words)
        user_guess: str = input("Guess: ")
        attempts -= 1
        guess_info: GuessInfo = check_guess(solution, user_guess)
        display_grid(extract_guess_letters(guess_info), attempts)
        


if __name__ == "__main__":
    main()