def conta_numero(numero,matriz):
    """Dado uma matriz e um número inteiro como entrada, retorna
    quantas vezes este número figura na matriz;
    int,list(list)->int"""
    cont=0
    for linha in matriz:
        for nu in linha:
            if nu==numero:
                cont+=1
    return cont