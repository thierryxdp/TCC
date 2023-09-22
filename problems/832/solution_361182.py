def eh_quadrada(matriz):
    '''retorna True se a amatriz for quadrada e False se não for;
    matriz->bool'''
    if len(matriz)==len(matriz[0]) or matriz==[]:
        return True
    else:
        return False