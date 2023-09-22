def conta_numero(numero, matriz):
    """
    Ao inserir uma número e uma matriz retorna a quantidade de vezes em
    que esse número aparece na matriz.
    int,list-> int
    """
    contador = 0
    for i in matriz:
        for j in i:
            if j == numero:
                contador+=1
    return contador