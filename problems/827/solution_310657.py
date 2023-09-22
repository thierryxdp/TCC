def qtd_divisores(x):
    for n in range(1,x):
        if (x+1%n) == 0:
            print(n)