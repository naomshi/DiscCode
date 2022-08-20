import logging
import tempfile
import json
import docker
from pathlib import Path
from enums import Difficulty, Language


class Result:
    success: bool
    message: str

    def __init__(self, success: bool, message: str):
        self.success = success
        self.message = message


class Challenge:
    difficulty: Difficulty
    language: Language
    challenge_name: str
    challenge_name_display: str
    description: str
    path: Path
    template: str


    def __init__(self, difficulty: Difficulty, challenge_name: str):
        self.difficulty = difficulty
        self.challenge_name = challenge_name
        self.language = Language.PYTHON
        self.path = Path("challenges/python/easy/add_two/")

        p = self.path.joinpath("metadata.json")
        p_json = json.loads(p.open(encoding="utf-8").read())

        self.challenge_name_display = p_json.get("name")
        self.description = p_json.get("description")

        self.template = self.path.joinpath("template.py").open().read()

        logging.info("Created new challenge %s of difficulty %s.", challenge_name, difficulty)


    def execute_attempt(self, attempt_content: str) -> Result:
        with tempfile.NamedTemporaryFile(mode="w+") as temp_f:
            attempt_file = Path(temp_f.name)

            attempt_file.write_text(attempt_content, encoding="utf8")

            cwd = Path().absolute()

            challenge_path = cwd.joinpath(
                f"challenges/{self.language.value}/{self.difficulty.value}/{self.challenge_name}"
            )

            volumes = {
                str(cwd.joinpath("challenges/run_challenge.py")): {
                    "bind": "/challenge/run_challenge.py", "mode": "ro"
                },
                str(challenge_path.joinpath("solution.py")): {
                    "bind": "/challenge/solution.py", "mode": "ro"
                },
                str(challenge_path.joinpath("test_cases.py")): {
                    "bind": "/challenge/test_cases.py", "mode": "ro"
                },
                str(attempt_file): {
                    "bind": "/challenge/attempt.py", "mode": "ro"
                },
            }

            client = docker.from_env()

            chall_result = client.containers.run(
                "challenge-python",
                volumes=volumes
            ).decode("utf-8").strip()

            return Result("successfully" in chall_result, chall_result)


if __name__ == "__main__":
    chall = Challenge(Difficulty.EASY, "add_two")

    attempt = """def solve(tup):
    return tup[0] - tup[1]
"""
    result = chall.execute_attempt(attempt)

    print(result.success, result.message)
