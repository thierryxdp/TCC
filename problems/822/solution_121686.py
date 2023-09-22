def repetidos(lista):
    """Calcula e Retorna o número de vezes que um elemento da lista é igual
       ao elemento anterior;
       list->int
       Parâmetros:
       lista: lista qualquer
    """
    i=0
    repetidos=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            repetidos=repetidos+1
        i=i+1
    return repetidos