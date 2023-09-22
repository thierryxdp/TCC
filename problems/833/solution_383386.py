def conta_numero(numero,matriz):
    """Esta função recebe um número inteiro e uma matriz e retorna a quantidade de vezes que este número aparece na matriz 
    int,list -> int"""
    lista = []
    for i in matriz:
        if i == numero:
            lista.append(i)
    return len(lista)