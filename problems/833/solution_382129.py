def conta_numero (numero,matriz):
    """funcao que dado um numero e uma matriz calcula e retorna quantas vezes
       esse numero aparece na matriz

       int,lista->lista
    """

    rep=0


    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                rep=rep+1

    return rep