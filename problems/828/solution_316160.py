def primo(n):
    lista = list(range(2,n))
    i = 0
    div = 0
    while i < len(lista):
        if n % lista[i] == 0:
            div = div + 1
        i = i + 1
        
    if div < 2:
        return False
    else:
        return True