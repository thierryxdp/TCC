def qtd_divisores(n):
    ls = []
for c in range(1,n+1):
    if n % c == 0:
        ls.append(c)
        return len(ls)