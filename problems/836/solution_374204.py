def busca(setor, matriz):

    '''
    Função que recebe uma matriz e uma string como parâmetro
    e retorna os todos os dados das linhas que possuem a string
    informada na chamada da  função.

    none, str -> list
    '''
    tam_linha = len(matriz)
    posicao_setor = 2 
    resp = []

    for i in range(tam_linha):
        if matriz[i][posicao_setor] == setor:
            proc = matriz[i]
            proc.remove(setor)
            resp.append(proc)
    return resp