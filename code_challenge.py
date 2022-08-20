from enums import Difficulty

class Challenge:
    difficulty: Difficulty

    def __init__(self, difficulty):
        print("Made a new challenge")