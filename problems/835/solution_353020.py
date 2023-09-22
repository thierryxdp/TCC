def melhor_volta(matriz):

    '''
    Função que recebe uma matriz como parâmetro e retorna
    a média dos termos da mesma.

    none -> float
    '''
    m_lin = matriz[0:]
    col = len(matriz[0])
    tam_linha = len(m_lin)
    
    m = []
    for x in range(tam_linha):
        mini = min(m_lin[x])
        m.append(mini)
    menor = (min(m))

    
    for i in range(tam_linha):
        for j in range(col):
            if m_lin[i][j] == menor:
                corredor = i+1
                volta = j+1
                       
    return (corredor, menor, volta)