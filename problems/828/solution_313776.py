def qnt_divisores(n):
    i = 1
    lista_de_divisores = []
    while i <= n:
        if n % i == 0:
            lista_de_divisores.append(i)
        i += 1
    return len(lista_de_divisores)

def primo(n):
    if qnt_divisores(n) == 2:
        return 'primo'
    else:
        return 'não primo'