def melhor_volta(matriz):
    """Dado uma matriz com os tempos em segundos dos corredores de um kart em cada volta, retorna quem fez a melhor volta da
    prova, tempo e em qual volta; list -> tupla"""
    coluna = len(matriz[0])
    linha = len(matriz)
    l = ()
    for i in range(linha):
        for j in range(coluna):
                m = matriz[i][j]
    melhor_v= min(m)
    return (melhor_v[i],melhor_v,melhor_v[i][j])