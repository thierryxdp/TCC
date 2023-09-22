def eh_quadrada(matriz):
    '''recebe uma matriz e retorna um valor booleano dizendo se a matriz é ou não é quadrada;list->boolean'''
    for m in range(len(matriz)):
        contadorlinha=0
        for n in range(len(matriz[0])):
            contadorcoluna=0
            contadorcoluna+=1
        contadorlinha+=1    
    if contadorlinha==contadorcoluna:
        return True
    else:
        return False