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

def main():
    A = "aacb"
    B = "caab"
    values = {
        'a': 2,
        'b': 4,
        'c': 5,
    }

    res, subsequence = hvlcs(A, B, values)
    print(res)
    print(subsequence)

if __name__ == "__main__":
    main()