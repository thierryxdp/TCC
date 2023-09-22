def eh_quadrada(matriz):
    '''
    Recebe uma matriz (lista de listas de números) e retorna se ela é quadrada ou não (mesmo número de linhas e colunas).
    list(list)-> bool
    
    Algoritmo:
    numero de linhas deve ser = numero de colunas
    checar se a len da matriz é zero
    se for:
    	quadrada
    se não:
    	checar a len da matriz
        checar a len de cada item da matriz
        para i e j na matriz:
        	retorna bool i == j
        
    '''
    i = len(matriz)
    if i == 0:
        return bool(i==0)
    else:
        j = len(matriz(0))
        return bool(i==j)