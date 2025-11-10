import json
import os

LEADERBOARD_FILE = "leaderboard.json"

def update_leaderboard(name, score):
    """Save or update player score in the leaderboard file."""
    data = {}

    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    # Update or add new player score
    data[name] = max(score, data.get(name, 0))

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_top_players(limit=5):
    """Return top players sorted by score (descending)."""
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    sorted_players = sorted(data.items(), key=lambda x: x[1], reverse=True)
    return sorted_players[:limit]
