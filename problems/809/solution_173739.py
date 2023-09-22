def intercala(lista1, lista2):
    '''Funcao que intercala duas listas
    e retorna uma terceira lista que e 
    formada intercalando as duas primeiras.
    Dados de entrada: list, list
    Valor de saida: list
    '''
    lista3 = []
    lista3.append(lista1[0])
    lista3.append(lista2[0])
    lista3.append(lista1[1])
    lista3.append(lista2[1])
    lista3.append(lista1[2])
    lista3.append(lista2[2])
    return lista3