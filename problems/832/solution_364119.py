def eh_quadrada(matriz):
    '''funcao que indentifica se uma matriz e quadrada
list->bool'''
    a=0
    for x in range(len(matriz)):
        a=a+1
        b=0
        for y in range(len(matriz[0])):
            b=b+1         
    if a==0:
        return True
    elif  len(matriz) == 1 and len(matriz[0]) == 0:
        return True
    else:
        return False