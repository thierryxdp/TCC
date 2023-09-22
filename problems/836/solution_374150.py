def busca(setor, matriz):

    '''
    Função que recebe uma matriz e uma string como parâmetro
    e retorna os todos os dados das linhas que possuem a string
    informada na chamada da  função.

    none, str -> list
    '''
    m_lin = matriz[0:]
    col = len(matriz[0])
    tam_linha = len(m_lin)

    result = []
    
    for i in range(tam_linha):
        for j in range(col):
            if m_lin[i][j] == setor:
                result.append(m_lin[i])
                       
    return result