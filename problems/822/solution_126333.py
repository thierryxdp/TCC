def repetidos (lista):
    """dada uma lista de numeros, retorna o numero de vezes que um elemento da lista e igual ao elemento anterior;
    list->int."""
    repete=0
    p=1
    while p<len(lista):
        if lista[p-1] == lista[p]:
            repete=repete+1
        p=p+1
    return repete