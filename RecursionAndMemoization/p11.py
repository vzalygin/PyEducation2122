import sys

L = sys.stdin.read().strip()

table = {}
def project(k, x):
    if (k, x) in table: return table[(k, x)]

    if k == 1: answer = L[x:x+1]
    else: answer = (project(k//2, x), project(k//2, x+k//2))

    table[(k, x)] = answer
    return answer

N = 1
while N < len(L): N *= 2
S = sorted(range(len(L)+1), key=lambda x: project(N, x))