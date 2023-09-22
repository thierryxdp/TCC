def melhor_volta(matriz):
    """Dado uma matriz com os tempos em segundos dos corredores de um kart em cada volta, retorna quem fez a melhor volta da
    prova, tempo e em qual volta; list -> tupla"""
    coluna = len(matriz[0])
    linha = len(matriz)
    for i in range(linha):
        for j in range(coluna):
            l = matriz[i][j]
            m = min(list.append(l))
    return (m[i],m,m[i][j])