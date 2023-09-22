#Exercício_05:
''' Essa função busca os dados das pessoas de um determinado setor de uma empresa. '''
#Exercício_05:
''' Essa função busca os dados das pessoas de um determinado setor de uma empresa. '''
''' (str, list) ---> list. '''

def busca(setor, matriz):
    
    nlin = len(matriz)
    ncol = len(matriz[0])
    list_result = []
    
    for i in range(nlin):
        for j in range(ncol):
            if matriz[i][j] == setor:
                list.remove(matriz[i],setor)
                list_result += [matriz[i]]
    return list_result