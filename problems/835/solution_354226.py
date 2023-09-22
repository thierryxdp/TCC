def melhor_volta(matriz):
    """Dado uma matriz com os tempos em segundos dos corredores de um kart em cada volta, retorna quem fez a melhor volta da
    prova, tempo e em qual volta; list -> tupla"""
    coluna = len(matriz[0])
    linha = len(matriz)
    for i in range(linha):
        for j in range(coluna):
            l = min(matriz[i][j])
   
    return (l[i],l,l[i][j])