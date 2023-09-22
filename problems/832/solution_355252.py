def eh_quadrada(matriz):
    '''recebe uma matriz e retorna um valor booleano dizendo se a matriz é ou não é quadrada;list->boolean'''
    listacoluna=[]
    listalinha=[]
    for m in range(len(matriz)):
        for n in range(len(matriz[0])):
            listacoluna.append(n)
        listalinha.append(m)
    if len(listalinha)==len(listacoluna):
        return True
    else:
        return False