def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D list to store lengths of longest common subsequence.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Building the dp matrix in bottom-up manner.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # dp[m][n] contains the length of LCS for str1[0..m-1], str2[0..n-1]
    # To find the actual LCS, we backtrack through dp.
    lcs_length = dp[m][n]
    lcs = [''] * lcs_length

    # Start from the right-most bottom cell and one by one store characters in lcs[]
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[lcs_length - 1] = str1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)

# Example usage:
if __name__ == "__main__":
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    lcs = longest_common_subsequence(str1, str2)
    print(f"The longest common subsequence is: {lcs}")