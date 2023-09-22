def repetidos(lista):
    """ Recebe uma lista numérica e retorna o numero de vezes em que um elemento dessa lista é igual ao elemento anterior;
    list->int """
    i=0
    soma=0
    while i<len(lista)-1:
        if lista[i+1]==lista[i]:
            soma=soma+1
        i=i+1
    return soma