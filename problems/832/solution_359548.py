def eh_quadrada(matriz):
    """Função que indentifica se uma matriz é quadrada ou não.
       list->bool"""
    for linha in range(0,len(matriz)):
        for coluna in range(0,len(matriz[linha])):
            if len(matriz[linha]) and len(matriz[coluna]) == len(matriz) :
                return True
            else:
                return False 
    return True