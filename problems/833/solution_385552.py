def conta_numero(numero,matriz):
    """função que dado um numero inteiro e uma matriz de inteiros, retorna quantas vezes 
    o numero aparece na matriz;
    int,list-->int"""
    cont = 0
    for i in matriz:
        for j in i:
            if numero == j:
                cont = cont + 1
    return cont