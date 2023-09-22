def repetidos(lista):
    """Dada uma lista de números, a função retorna a quantidade de vezes
    que um elemento da lista é igual ao seu anteior.
    Patametros de Entrada:lis
    Retorna: int"""

    i=1
    contador=0

    while i< len(lista):
        if lista[i]== lista[i-1]:
            contador+=1
        i+=1
    return contador