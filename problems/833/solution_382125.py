def conta_numero (numero,matriz):
    """funcao que dado um numero e uma matriz calcula e retorna quantas vezes
       esse numero aparece na matriz

       int,lista->lista
    """

    nlinhas= len(matriz)
    ncolunas=len(matriz[0])
    rep=0


    for i in range(nlinhas):
        for j in range(ncolunas):
            if numero == matriz[i][j]:
                rep=rep+1

    return rep