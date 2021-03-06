'''
문제
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

입력
첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

출력
첫째 줄에 경우의 수를 출력한다.

3
'''
n = int(input())

d = [0] * 31
d[2] = 3


# n 이 홀수 일 때: 짝수인 타일로 채울 수 없으므로 d[n]= 0

# n = 2 일 때
# 경우의 수 = 3

# n = 4 일 때
# 경우의 수 = 3 * 3 + 2 = 11

# n = 4 일 때
# 경우의 수 = 11 * 3 + 3 * 2 + 2
# .
# .
# .
# d[n] = d[n - 2] * 3 + [n - 4] * 2 + dn - 6] * 2 +
#        ・・・ + d[2] * 2 + 2(n일 떄만의 경우 2가지)


for i in range(4, n + 1, 2):
    d[i] = d[i - 2] * 3 + sum(d[:i-2]) * 2 + 2


print(d[n])
