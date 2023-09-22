def repetidos (lista_num):
    """função que recebe uma lista numérica (lista_num) e que deve
    retornar o número de vezes que um elemento da lista é repetido;
    lista->int"""
    i = 0
    while lista_num[i]!=lista_num[i+1]:
         i = i+1
    return i