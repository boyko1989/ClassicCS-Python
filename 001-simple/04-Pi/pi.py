def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0

    return pi

if __name__ == "__main__":
    print(calculate_pi(1000000))      # 3.1415916535897743
    # print(calculate_pi(10000000))   # 3.1415925535897915
    # print(calculate_pi(100000000))  # 3.141592643589326
    # print(calculate_pi(1000000000)) # 3.1415926525880504