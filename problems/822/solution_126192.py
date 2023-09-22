def repetidos(lista):
    """
    Retorna o numero de vezes que um elemento da lista é igual ao anterior.
    list -> int
    """
    i=0
    repeticao=0
    while i+1<len(lista):
        if lista[i]==lista[i+1]:
            repeticao= repeticao+1
        i= i+1
    return repeticao