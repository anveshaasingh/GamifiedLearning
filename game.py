

from GamifiedLearning.player import Player
from GamifiedLearning.levels import init_levels

def show_intro():
    print("="*40)
    print("   QUIZ ADVENTURE: Learn by Playing")
    print("="*40)
    print("Answer questions to progress through levels.")
    print("You have limited lives. Use hints ('h').\n")

def show_status(player, total_levels):
    print(f"\n--- Player: {player.name} | Level {player.current_level+1}/{total_levels} | Lives: {player.lives} ---")
    print("Badges:", player.badges if player.badges else "none")

def ask_question(question, player):
    while True:
        print("\n" + question["prompt"])
        for i, choice in enumerate(question["choices"], 1):
            print(f"  {i}) {choice}")

        user_input = input("Enter choice number (or 'h' for hint, 's' to save & quit): ").strip().lower()

        if user_input == "h":
            print("Hint:", question.get("hint", "No hint available."))
            continue
        if user_input == "s":
            player.save()
            print("Progress saved. Exiting...")
            exit()

        if not user_input.isdigit():
            print("Invalid input, try again.")
            continue

        choice = int(user_input) - 1
        return choice == question["answer"]

def award_badge(player, level_index):
    badge = f"Badge-{level_index+1}"
    if badge not in player.badges:
        player.badges.append(badge)
        print(f"\n*** Achievement unlocked: {badge}! ***")

def run_game():
    levels = init_levels()
    player = None

    choice = input("Load previous progress? (y/n): ").strip().lower()
    if choice == "y":
        player = Player.load()
        if player:
            print(f"Loaded player {player.name}.")
        else:
            print("No save found, creating new player.")
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
        print(f"\n*** Congratulations {player.name}, you finished the game! ***")
        print("Badges:", player.badges)
    player.save()
