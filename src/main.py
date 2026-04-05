import random

def hvlcs(A, B, values):
    m = len(A)
    n = len(B)
 
    dp = [[0] * (n + 1) for i in range(m + 1)]
    
    # Calculating the Value
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If character is the same, add the value of character
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + values[A[i - 1]]
            # If character is different, take the string with max score
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Getting the Optimal Subsequence (Backtracking)
    i, j = m, n
    subsequence = ""
    while i >= 0 and j >= 0:
        if dp[i][j] != dp[i - 1][j] and dp[i][j] != dp[i][j - 1]:
            subsequence += A[i - 1]
            i, j = i - 1, j - 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1

    subsequence = subsequence[::-1]

    return dp[m][n], subsequence

def read_input(file_path):
    with open(file_path, "r") as f:
        num_of_letters = int(f.readline())
        values = {}

        for _ in range(num_of_letters):
            letter, value = f.readline().split()
            values[letter] = int(value)
        
        A = f.readline().strip()
        B = f.readline().strip()
    
    return A, B, values

def write_output(file_path, res, subsequence):
    with open(file_path, "w") as f:
        f.write(str(res) + "\n")
        f.write(subsequence)

def create_tests(alphabet_size=10):
    random.seed(10)
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for i in range(10):
        chars = alphabet[:alphabet_size]
        values = {c: random.randint(1, 10) for c in chars}

        length = (i + 1) * 25
        A = ''.join(random.choices(chars, k=length))
        B = ''.join(random.choices(chars, k=length))

        lines = [str(alphabet_size)]
        for c, v in values.items():
            lines.append(f"{c} {v}")
        lines.append(A)
        lines.append(B)
        content = '\n'.join(lines)

        filename = f"../tests/test{i + 1}.in"
        with open(filename, "w") as f:
            f.write(content)

def run_tests():
    base_name = "../tests/"
    test_files = [f"test{i+1}" for i in range(10)]

    for file in test_files:
        input_file = base_name + file + ".in"
        output_file = base_name + file + ".out"

        A, B, values = read_input(input_file)
        max_val, subseq = hvlcs(A, B, values)

        with open(output_file, "w") as f:
            f.write(f"{max_val}\n")
            f.write(f"{subseq}\n")


def main():
    user_choice = input("Would you like to run custom or standard tests? [custom/standard] ")

    if user_choice.lower() == "custom":
        base = "../data/"
        input_path = base + "input.in"
        output_path = base + "output.out"

        A, B, values = read_input(input_path)
        res, subsequence = hvlcs(A, B, values)

        print(str(res) + "\n" + subsequence)
        write_output(output_path, res, subsequence)

    elif user_choice.lower() == "standard":
        if not os.path.exists("../tests/test1.in"):
            create_tests()
        run_tests()

if __name__ == "__main__":
    main()