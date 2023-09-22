def eh_quadrada(matriz):
    '''funcao que retorna um valor booleano dizendo se a matriz e quadrada ou nao; list->bool'''
    if len(matriz)>0 and len(matriz)==len(matriz[0]):
            return True
    elif matriz==[]:
            return True
    else:
        return False