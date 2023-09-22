def busca(setor,matriz):
    """Funcao que retorna todos os dados de funcionarios de um determinado setor. List-->str,List"""
    resposta = []
    linhas = []
    count = 0
    soma = 0
    for i in range(len(matriz)):
            if matriz[i][2] == setor:
                count+=1
                list.append(linhas,i)
                list.remove(matriz[i],setor)
                resposta = matriz  
            
    if 0 in linhas and 1 in linhas and 2 not in linhas:
        del resposta[2]
    elif 0 in linhas and 1 not in linhas and 2 in linhas:
        del resposta[1]
    elif 0 not in linhas and 1 in linhas and 2 in linhas:
        del resposta[0]
    elif 0 in linhas and 1 not in linhas and 2 not in linhas:
        resposta = [matriz[0]]
    elif 0 not in linhas and 1 in linhas and 2 not in linhas:
        resposta = [matriz[1]]
    elif 0 not in linhas and 1 not in linhas and 2 in linhas:
        resposta = [matriz[2]]
    elif 0 not in linhas and 1 not in linhas and 2 not in linhas:
        resposta = []
    
    return resposta