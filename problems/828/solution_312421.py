def primo(n):
    pos = 0
    lista_divisores = []
    lista = list(range(n+1))
    for elemento in lista:
        if n%(elemento+1) == 0:
            list.append(lista_divisores,n/(elemento+1))
        pos = pos + 1
    if len(lista_divisores) == 2:
        return True
    else:
        return False