def repetidos(n):
    """funcao que recebe uma lista de numeros e retorna quantas vezes um elemento da lista e igual ao elemento anterior
    list -> int"""
    i=0
    d=0
    while i < len( n):
        if n[i]==n[i-1]:
            d=d+1
        i=i+1
    return d