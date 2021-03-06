'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

4
'''

n = int(input())
array = list(map(int, input().split()))

# 자신을 포함한 수열의 수를 저장할 배열 초기화
d = [0] * n

# 자신과 이전의 원소를 비교했을 때
for i in range(n):
  for j in range(i):
    # j번째 원소가 자신보다 작은수이면
    if array[i] > array[j]:
      # j의 값 + 1(자신을 포함한 경우), 현재 자신을 값 중 큰 수를 선택
      d[i] = max(d[i], d[j] + 1)

# 가장 큰 경우 출력
print(max(d))