def qtd_divisores(x):
    count = 0
    for num in range(1,x+1):
        if x%num == 0:
            return count