def repetidos(lista):
    """Função que retorna  o número de vezes que um elemento da lista
é igual a seu antecessor; list -> int"""
    cont=1
    vezes=0
    while cont<len(lista):
        if lista[cont]==lista[cont-1]:
            cont+=1
            vezes+=1
        else:
            cont+=1
    return vezes