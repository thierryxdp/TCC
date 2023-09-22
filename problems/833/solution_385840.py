def conta_numero(numero,matriz):
    """dado um numero inteiro e uma matriz de inteiros de
    tamanho qualquer,conta e retorna quantas vezes aquele
    numero aparece na matriz.
    int,list(of lists)->int"""
    x=0
    for linha in matriz:
        for num in linha:
            if num==numero:
                x+=1
    return x