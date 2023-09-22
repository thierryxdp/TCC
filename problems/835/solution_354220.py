def melhor_volta(matriz):
    """Dado uma matriz com os tempos em segundos dos corredores de um kart em cada volta, retorna quem fez a melhor volta da
    prova, tempo e em qual volta; list -> tupla"""
    coluna = len(matriz[0])
    linha = len(matriz)
    c1=[],c2=[],c3=[],c4=[],c5=[] e c6=[]
    for i in range(linha):
        for j in range(coluna):
                l = matriz[i][j]
                if i = 0:
                    list.append(c1)
                if i= 1:
                    list.append(c2)
                if i = 2:
                    list.append(c3)
                if i = 3:
                    list.append(c4)
                if i= 4:
                    list.append(c5)
                if i= 5:
                    list.append(c6)