def insere(lista_num,n):
    '''função que recebe uma lista numérica (lista_num) de 
    ordem crescente e que também recebe um número (n). E que
    retorna uma lista nova que contenha o número de entrada,
    tal que a lista continue ordenada, ou seja,crescente;
    lista, int->lista'''
    list.insert(lista_num,0,n)
    list.sort(lista_num)
    return lista_num