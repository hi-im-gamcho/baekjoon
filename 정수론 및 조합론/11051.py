import sys
from math import factorial

input = sys.stdin.readline

N, K = map(int, input().split())

result = factorial(N) // factorial(K) // factorial(N-K)

print(result % 10007)