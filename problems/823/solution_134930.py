def faltante (n):
    nCrescente=sorted(n)
    i=0
    while i < len(nCrescente):
        if i+1 != nCrescente[i]:
            return i+1
        i=i+1
    return len(nCrescente) + 1
'''funçao que recebe uma lista numeros inteiros
com tamanho n, e retorna o numero que esta faltando
na lista dada como parametro
list->int'''