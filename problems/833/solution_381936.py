def conta_numero(numero, matriz):
    """Função que retorna a quantidade de vezesque um determinado numero apareceu numa matriz;
    int,list-> int"""
    contador = 0
    for i in matriz:
        for j in i:
            if j == numero:
                contador+=1
    return contador