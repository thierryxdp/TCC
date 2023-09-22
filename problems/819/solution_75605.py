def filtraMultiplos(lista,n):
    """Filtra os múltiplos de um número n. Recebe como entrada uma lista de números e um número, e retornar outra lista contendo todos os elementos da lista original que forem divisíveis por n.
    lista,float-->lista"""
    multiplos=[]
    posicao=0
    while posicao < len(lista):
        if lista[posicao]%n==0:
            list.append(multiplos, lista[posicao])
        posicao=posicao+1
    return multiplos