def posLetra(texto,l,n):
    if texto.count(l)<n:
        return -1
    contador = 0
    extensao = len(texto)
    atual = 0
    while contador < extensao and atual <= n:
        if texto[contador] == l:
            atual = contador
        contador = contador+1
    return atual