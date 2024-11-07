import unittest

def optimal_bst(keys, freq, n):
    # Дэд асуудлын үр дүнг хадгалах 2D хүснэгт
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # давтамжийн нийлбэрийг хадгалах хүснэгт
    freq_sum = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        freq_sum[i][i] = freq[i]  # single key
        for j in range(i + 1, n):
            freq_sum[i][j] = freq_sum[i][j - 1] + freq[j]  # i-ээс j хүртэлх давтамжийн нийлбэр
            
            print(f"Current freq_sum: {freq_sum[i][j - 1]} + {freq[j]}")
            print(f"Total frequency sum for keys from {i} to {j}: {freq_sum[i][j]}")

    # Нэг гол модны хувьд dp хүснэгт
    for i in range(n):
        dp[i][i] = freq[i]
        # print(dp[i][i])

    # 2-оос n урттай гинжний хувьд dp хүснэгт
    for length in range(2, n + 1):  
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            # Түлхүүр бүрийг [i, j] интервалаар үндэс болгоно
            for root in range(i, j + 1):
                left_cost = dp[i][root - 1] if root > i else 0
                right_cost = dp[root + 1][j] if root < j else 0
                total_cost = left_cost + right_cost + freq_sum[i][j]

                print(f"root: {root}:")
                print(f"Left cost (dp[{i}][{root - 1}]): {left_cost}")
                print(f"Right cost (dp[{root + 1}][{j}]): {right_cost}")
                print(f"давтамжийн_нийлбэр (freq_sum[{i}][{j}]): {freq_sum[i][j]}")
                print(f"{root} Root дээрх зардал : {total_cost}")

                if total_cost < dp[i][j]:
                    dp[i][j] = total_cost
                    print(f"Updated dp[{i}][{j}] to {dp[i][j]} with root {root}")

    return dp[0][n - 1]




class TestOptimalBST(unittest.TestCase):
    
    def test_specific_case(self):
        keys = [5, 6]
        freq = [17, 25]
        n = len(keys)
        expected_cost = 59
        self.assertEqual(optimal_bst(keys, freq, n), expected_cost)


if __name__ == '__main__':
    unittest.main()