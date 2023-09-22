def qtd_divisores(n):
    i = 0
    for x in range(n):
        if n[i]%n == 0:
            return n
        i +=1