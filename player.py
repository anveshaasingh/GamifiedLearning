
import json
import os

class Player:
    def __init__(self, name="Player", lives=3, current_level=0, badges=None):
        self.name = name
        self.lives = lives
        self.current_level = current_level
        self.badges = badges if badges else []

    def save(self):
        data = {
            "name": self.name,
            "lives": self.lives,
            "current_level": self.current_level,
            "badges": self.badges,
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)
        print("Progress saved successfully!")

    @staticmethod
    def load():
        if not os.path.exists(SAVE_FILE):
            return None
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        return Player(**data)
