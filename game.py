from player import Player
from levels import init_levels
from leaderboard import get_top_players


def show_intro():
    print("=" * 45)
    print("     GAMIFIED LEARNING: A QUESTION-DRIVEN EXPLORATION EXPERIENCE")
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
        name = input("Enter your name: ").strip()
        player = Player.load(name)
        if player:
            if player.lives <= 0:  # reset lives if player was dead
                player.lives = 3
            print(f"Welcome back, {player.name}! Resuming your progress...")
        else:
            print("No saved data found. Starting a new game.")
            player = Player(name=name)
    else:
        name = input("Enter your name: ").strip()
        player = Player(name=name)


    show_intro()

    while player.current_level < len(levels) and player.lives > 0:
        show_status(player, len(levels))
        level = levels[player.current_level]

        print(f"\n--- Level {player.current_level+1}: {level['title']} ---")
        print(level["narrative"])

        if ask_question(level["question"], player):
            print("Correct!\n")
            award_badge(player, player.current_level)
            player.score += 10
            player.current_level += 1
            player.save()
        else:
            print("Wrong! You lost a life.\n")
            player.lives -= 1
            if player.lives <= 0:
                print("*** Game Over! ***")
                break

    # After the game ends
    if player.current_level >= len(levels):
        print(f"\n🎉 Congratulations {player.name}, you finished all levels! 🎉")
    else:
        print("💀 Game Over!")

    print(f"Score: {getattr(player, 'score', player.current_level * 10)}, Badges: {player.badges}")
    player.save()

    # Show leaderboard
    print("\n🏆 Leaderboard:")
    for i, (name, score) in enumerate(get_top_players(), start=1):
        print(f"{i}. {name} - {score} points")


# This line must be OUTSIDE all functions (at the end)
if __name__ == "__main__":
    run_game()

