def conta_numero (numero,matriz):
    """funcao que dado um numero e uma matriz calcula e retorna quantas vezes
       esse numero aparece na matriz

       int,lista->lista
    """

    nlinhas= len(matriz)
    ncolunas=len(matriz[0])
    rep=0

    if len(matriz)==0:
        return 0

    else:
        for i in range(nlinhas):
            for j in range(ncolunas):
                if numero == matriz[i][j]:
                    rep=rep+1
                    return rep