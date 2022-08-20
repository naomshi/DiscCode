import solution
import attempt
import test_cases

def main():
    solution_results = []
    attempt_results = []

    for case in test_cases:
        solution_results.append(solution.solve(case))
        attempt_results.apend(attempt.solve(case))

    for solution_result, attempt_result in zip(solution_results, attempt_results):
        if solution_result != attempt_result:
            print("fail")
            return
    
    print("win")


if __name__ == "__main__":
    main()
