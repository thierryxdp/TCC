def qtd_divisores(x):
    for num in range(1,x):
        if x%num == 0:
            return [num]