def repetidos(lista):
    """dado uma lista de númros, a função retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior;
    list->int"""
    contador=0
    indice=1
    while indice <= (len(frase)-1):
        if lista[indice]==lista[indice-1]:
            contador=contador+1
        else:
            contador=contador
        indice=indice+1
    return contador