def repetidos(lista):
    """dada uma lista de números, a função retorna a quantidade de vezes
    que um elemento da lista é igual ao elemento anterior a ele.
    list-->int
    
    Parâmetros
    lista: lista de números utilizada como entrada"""
    indice=0
    contador=0
    while indice<len(lista):
        if lista[indice]==lista[indice-1]:
            contador=contador+1
        indice=indice+1
    return contador