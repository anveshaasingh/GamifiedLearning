
import json, os

import json, os

class Player:
    def __init__(self, name="Player", lives=3, current_level=0, badges=None, score=0):
        self.name = name
        self.lives = lives
        self.current_level = current_level
        self.badges = badges if badges else []
        self.score = score   # ✅ Added score attribute here

    def save(self):
        """Save player progress to a JSON file (multi-player supported)."""
        all_data = {}
        if os.path.exists("save.json"):
            with open("save.json", "r") as f:
                try:
                    all_data = json.load(f)
                except json.JSONDecodeError:
                    all_data = {}

        all_data[self.name] = {
            "name": self.name,
            "lives": self.lives,
            "current_level": self.current_level,
            "badges": self.badges,
            "score": self.score,     # ✅ Save the score
        }

        with open("save.json", "w") as f:
            json.dump(all_data, f, indent=4)
        print("Progress saved successfully!")

        # ✅ Update leaderboard when saving
        from leaderboard import update_leaderboard
        update_leaderboard(self.name, self.score)

    @staticmethod
    def load(name):
        """Load saved player data by name."""
        if not os.path.exists("save.json"):
            return None
        try:
            with open("save.json", "r") as f:
                data = json.load(f)
            if name in data:
                return Player(**data[name])
        except Exception as e:
            print("Error loading save file:", e)
        return None

    
