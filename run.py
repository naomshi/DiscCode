import docker
import pathlib

client = docker.from_env()

cwd = pathlib.Path().absolute()

volumes = {
    str(cwd.joinpath("challenges/run_challenge.py")): {"bind": "/challenge/run_challenge.py", "mode": "ro"},
    str(cwd.joinpath("challenges/python/easy/add_two/solution.py")): {"bind": "/challenge/solution.py", "mode": "ro"},
    str(cwd.joinpath("challenges/python/easy/add_two/test_cases.py")): {"bind": "/challenge/test_cases.py", "mode": "ro"},
    str(cwd.joinpath("attempt.py")): {"bind": "/challenge/attempt.py", "mode": "ro"},
}

result = client.containers.run("challenge-python", volumes=volumes)

print(result.decode("utf-8"))