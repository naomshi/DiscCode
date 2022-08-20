from enums import Difficulty, Language
import logging

class Challenge:
    difficulty: Difficulty
    language: Language

    def __init__(self, difficulty):
        logging.info(f"Created new challenge of difficulty {difficulty}.")

    
    def spawn_container(self):
