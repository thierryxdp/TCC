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
                dados = [[matriz[i][0], [matriz[i][1], [matriz[i][3]]
                list_result += [dados]
    return list_result