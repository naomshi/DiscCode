import solution
import attempt
from test_cases import cases

def main():
    for case in cases:
        solution_solve = solution.solve(case)
        attempt_solve = attempt.solve(case)

        if solution_solve != attempt_solve:
            print(f"Failed: Test case {case} failed with result {attempt_solve}.")
            return

    print("Tests all completed successfully! Congratulations.")


if __name__ == "__main__":
    main()
