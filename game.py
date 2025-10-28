from player import Player
from levels import init_levels

def show_intro():
    print("=" * 45)
    print("     QUIZ ADVENTURE: Learn by Playing")
    print("=" * 45)
    print("Answer questions to clear levels and earn badges!")
    print("Each wrong answer loses one life (3 total).\n")

def show_status(player, total_levels):
    print(f"\nPlayer: {player.name} | Level {player.current_level+1}/{total_levels} | Lives: {player.lives}")
    print("Badges:", player.badges if player.badges else "none")

def ask_question(question, player):
    while True:
        print("\n" + question["prompt"])
        for i, choice in enumerate(question["choices"], 1):
            print(f"  {i}) {choice}")

        user_input = input("Enter number (or 'h' for hint, 's' to save & quit): ").strip().lower()

        if user_input == "h":
            print("Hint:", question.get("hint", "No hint available."))
            continue
        if user_input == "s":
            player.save()
            print("Progress saved. Exiting game...")
            exit()

        if not user_input.isdigit():
            print("Invalid input. Try again.")
            continue

        choice = int(user_input) - 1
        if choice < 0 or choice >= len(question["choices"]):
            print("Choice out of range.")
            continue

        return choice == question["answer"]

def award_badge(player, level_index):
    badge = f"Badge-{level_index+1}"
    if badge not in player.badges:
        player.badges.append(badge)
        print(f"\n*** Achievement Unlocked: {badge}! ***")

def run_game():
    levels = init_levels()
    player = None

    choice = input("Load previous progress? (y/n): ").strip().lower()
    if choice == "y":
        player = Player.load()
        if player:
            print(f"Welcome back, {player.name}!")
        else:
            player = Player(name=input("Enter your name: ").strip())
    else:
        player = Player(name=input("Enter your name: ").strip())

    show_intro()

    while player.current_level < len(levels) and player.lives > 0:
        show_status(player, len(levels))
        level = levels[player.current_level]

        print(f"\n--- Level {player.current_level+1}: {level['title']} ---")
        print(level["narrative"])

        if ask_question(level["question"], player):
            print("Correct!\n")
            award_badge(player, player.current_level)
            player.current_level += 1
            player.save()
        else:
            print("Wrong! You lost a life.\n")
            player.lives -= 1
            if player.lives <= 0:
                print("*** Game Over! ***")
                break

    if player.current_level >= len(levels):
        print(f"\n*** Congratulations {player.name}, you finished all levels! ***")
        print("Your badges:", player.badges)
    player.save()

if __name__ == "__main__":
    run_game()



