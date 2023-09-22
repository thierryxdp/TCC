def qtd_divisores(n):
    divisores = 1
    for divisores in list.range(1,21):
        n//divisores
    return len(divisores)