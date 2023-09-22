def filtraMultiplos(lista,n):
    """recebe como entrada uma lista de números, e retorna o número de vezes que um elemento da lista ́e igual ao elemento anterior"""
    resposta=()
    i=0
    while i<len(lista):
        if int(lista[i])%n==0:
            add=str(lista[i])
            resposta=resposta+tuple(add)
        i=i+1
    return list(resposta)