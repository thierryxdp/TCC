def eh_quadrada(matriz):
    '''funcao que indentifica se uma matriz e quadrada
list->bool'''
    a=0
    b=0
    for x in range(len(matriz)):
        a=a+1
        for y in range(len(matriz[x])):
            b=b+1
    if a==b:
        return True
    else:
        return False