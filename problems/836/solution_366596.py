def busca(string, matriz):
    '''recebe uma string referente ao setor da empresa e uma matriz que
    armazena os dados dos funcionários dessa empresa, retorna os dados de
    todos os funcionários da empresa
    string, list ->list'''
    retorna =[]
    for i in range(len(matriz)):
        
            if string ==matriz[i][2]:
                retorna.append(matriz[i].remove(string))
                
    return retorna