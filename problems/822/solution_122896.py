def repetidos(lista):
    """Funcao que recebe como entrada uma lista de numeros e retorna 
    o numero de vezes que determinado elemento da lista e igual ao anterior"""
    contador=0
    vezes=0
    while contador< len(lista)-1:
        if lista[contador+1] == lista[contador]:
            vezes += 1
    return vezes