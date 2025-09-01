from word_list import words
import random
from typing import TypedDict

class GuessInfo(TypedDict): # so the type checker won't complain
    isPerfect: bool
    result_letters: list[str]

def display_grid(letters: list[str], attempts: int) -> None:
    
    """
    displays the wordle grid in the format
    _____________________
    | 1 | 2 | 3 | 4 | 5 |
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """

    print("_____________________")
    print(f"| {letters[0]} | {letters[1]} | {letters[2]} | {letters[3]} | {letters[4]} |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print(f"Attempt: {attempts}/5")

def check_guess(user_guess: str, solution: str) -> GuessInfo:
    
    """
    If a letter of the user_guess is in solution and in the correct place, wrap the letter with ⸨⸩. If letter of user_guess is in solution but not in the correct place, wrap with []. Otherwise if the letter is not in word the word at all, wrap with --.
    """

    correct_letters: int = 0
    guess_info: GuessInfo = {
        "isPerfect": False,
        "result_letters": [], # 5 spaces for 5 letters 
    }

    """
    # Comment these 2 lines out when not doing testing to avoid the solution being spoiled!
    print(f"user_guess: {user_guess}")
    print(f"solution: {solution}")
    """

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
    solution: str = random.choice(words)
    print("--------- WORDLE ULTRALITE ---------")

    while can_guess:
        if attempts < 5:
            user_guess: str = input("Guess: ")
            if len(user_guess) != 5:
                print("The word needs to have 5 letters!")

            else:
                attempts += 1
                guess_info: GuessInfo = check_guess(user_guess.upper(), solution.upper())
                display_grid(guess_info["result_letters"], attempts)
                # end game - success
                if guess_info["isPerfect"]:
                    print("Congratulations for guessing the word!")
                    play_again: str = input("Would you like to play another round? (Y/N) ")
                    if play_again.upper() == "Y":
                        solution = random.choice(words)
                        attempts = 0
                    else:
                        print("Thanks for playing!")
                        can_guess = False
        else:
            # end game - fail
            play_again: str = input("Sorry, you ran out of guesses! Would you like to play again? (Y/N) ")
            if play_again.upper() == "Y":
                attempts = 0
                solution = random.choice(words)
            else:
                print("Thanks for playing!")
                can_guess = False

"""
--- Test cases and notes ---
6 letter word: Freaks
Result: As intended, player gets message to enter 5 letter words and is able to continue playing

Word with 2 of the same letter: Green
Result: "| ⸨G⸩ | ⸨R⸩ | ⸨E⸩ | [N] | [E] |", if player enters "GREEE", the program will mark the first 2 E's as correct, but will also mark the last E as in the word as well

TODO: Possible fix: List of "letters remaining" - For each guess, with a list of letters remaining, the program will remove the letters that have been already verified
"""

if __name__ == "__main__":
    main()