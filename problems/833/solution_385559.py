#Exercício_02:
''' Essa função conta quantas vezes um número repete em determinada matriz. '''
''' float, list ---> int. '''

def conta_numero(number, matriz):
    if matriz == []:
        return 0
    else:
        nlin = len(matriz)
        ncol = len(matriz[0])
        list_numbers = []
    
        for i in range(nlin):
            for j in range(ncol):
                list_numbers += [matriz[i][j], ]
    
        quantidade = list.count(list_numbers, number)
        return quantidade