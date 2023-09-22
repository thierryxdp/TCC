def intercala(lista1, lista2):
    '''
    	Função que, dados os parâmetros de entrada
        lista1 e lista2, retorna uma nova lista, 
        com os elementos da lista1 e da lista2
        intercalados
        : param lista1: list
        : param lista2: list
        : return: list
    '''
    return lista1[0:1] + lista2[0:1] + lista1[1:2] + lista2[1:2] + lista1[2:3] + lista2[2:3] + lista1[3:] + lista2[3:]