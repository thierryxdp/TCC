def repetidos(lista):
    """Recebe uma lista de números e retorna o número de vezes
    que um elemnto da lista é igual ao elemnto anterior.
    Assinatura: list --> int"""
    
    contador=0
    lista2=lista[1:]
    for n in range(len(lista)):
        if lista[n] == lista2[n]:
            contador+= 1
    return contador