def eh_quadrada(matriz):
    '''recebe uma matriz e retorna um valor booleano dizendo se a matriz é ou não é quadrada;list->boolean'''
    linha=len(matriz)
    for m in range(len(matriz)):
        for n in range(len(matriz[0])):
        	listacoluna.append(n)
        coluna=max(listacoluna)+1    
    if linha==coluna:
        return True
    else:
        return False