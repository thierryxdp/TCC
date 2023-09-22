def repetidos(lista):
    """retorna o número de vezes que um elemento da lista é igual ao elemento anterior.
    list->int"""
    qntd=0
    indice=1
    while indice<len(lista):
        if lista[indice]==lista[indice-1]:
            qntd=qntd+1
        indice+=1
    return qntd