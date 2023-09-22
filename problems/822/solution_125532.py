def repetidos(lista):
    """Retorna quantas vezes que um elemento da lista é igual ao elemento anterior; list->int"""
    i=1
    acumulador=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            acumulador+=1
        i+=1
    return acumulador