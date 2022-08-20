from enums import Difficulty, Language
import logging


class Result:
    success: bool
    message: str


class Challenge:
    difficulty: Difficulty
    language: Language


    def __init__(self, difficulty):
        logging.info(f"Created new challenge of difficulty {difficulty}.")


    def execute_attempt(self) -> Result:
        
