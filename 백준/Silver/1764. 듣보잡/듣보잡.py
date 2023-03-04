M, N = map(int, input().split())

dic = dict()
for i in range(1, M + 1):
    stdin = input()
    dic[stdin] = 0

for i in range(N):
    stdin = input()
    if stdin in dic:
        dic[stdin] = 1

res = sorted([key for key,_ in filter(lambda x: x[1], dic.items())])
print(len(res))
print(*res, sep='\n')