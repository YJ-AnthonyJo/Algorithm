M, N = map(int, input().split())


Dic = dict()
for i in range(1, M + 1):
    Dic[input()] = str(i)

inv_dic = {v:k for k, v in Dic.items()}
for i in range(N):
    stdin = input()
    if stdin.isdecimal():
        print(inv_dic[stdin])
    else :
        print(Dic[stdin])
    