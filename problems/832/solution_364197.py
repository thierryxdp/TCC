def eh_quadrada (matriz):
    '''função que identifica se uma matriz é quadrada,retorna
    True se for e False se não;list->bool'''
    for i in matriz:
        linha=(len(matriz))
        col=(len(matriz[0]))
        teste=[]
        if (len(teste))==(len(matriz)):
            return True
        else:
            if linha == col:
            	return True
            else:
                return False