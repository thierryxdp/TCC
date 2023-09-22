def eh_quadrada(lista):
    ''' funcao que dado uma metriz diz se eh uma matriz quadrada
    lista->bool'''
    if lista == []:
        return True
    elif len(lista) == len(lista[0]):
        return True
    else:
        return False