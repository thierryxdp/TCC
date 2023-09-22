def busca(setor, matriz):

    '''
    Função que recebe uma matriz e uma string como parâmetro
    e retorna os todos os dados das linhas que possuem a string
    informada na chamada da  função.

    none, str -> list
    '''
    tam_linha = len(matriz)
    col = len(matriz[0]) 
    resp = []

    
    for i in range(tam_linha):
        for j in range(col):
            if setor in matriz[i][j]:
                num_setor = j
                    
    for i in range(tam_linha):
        if matriz[i][num_setor] == setor:
            proc = matriz[i]
            proc.remove(setor)
            resp.append(proc)
            
            
    return resp