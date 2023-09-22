def repetidos(lista_numros):

    """Função que dada uma lista números retorna a quantidade de vezes que os número são repetidos.

    list -> int"""

    indice = 0

    iguais = 0

    while indice < len(lista_numeros):

        if lista_numeros[indice] == lista_numeros[indice + 1]:

            iguais +=1

   



        indice += 1

    return iguais