def repetidos(lista):
    """função que retorna o numero de vezes que um numero é igual ao anterior; list->int """
    i=1
    contador= 0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            contador+=1
        i+=1
    return contador