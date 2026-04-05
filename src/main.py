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
        
        A = f.readline()
        B = f.readline()
    
    return A, B, values

def write_output(file_path, res, subsequence):
    with open(file_path, "w") as f:
        f.write(str(res) + "\n")
        f.write(subsequence)

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
        base = "../tests/"
        num_of_test_files = 1

        for num in range(num_of_test_files):
            input_path = f"{base}test{num + 1}.in"
            output_path = f"{base}test{num + 1}.out"

            A, B, values = read_input(input_path)
            res, subsequence = hvlcs(A, B, values)
            write_output(output_path, res, subsequence)

if __name__ == "__main__":
    main()