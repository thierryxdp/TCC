def repetidos(lista): 
    """Recebe uma lista de números e retorna o número de de vezes que um elemento da lista é igual ao elemento anterior. Assinatura:list --> int"""
    
    contador=0 
    lista=lista[1:]
    for n in range(len(lista)-1):
        if lista[n] == lista2[n]:
            contador+= 1 
    return contador