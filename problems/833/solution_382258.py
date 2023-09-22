def conta_numero(numero, matriz):
    """ Numero inteiro e uma matriz de inteiros retorna quantas vezes aparece o
    numero na matriz
    int-> int"""
    quantidade=[]
    for lista in matriz:
        for i in lista:
            if i==numero:
                cont= cont +1
        list.append(quantidade,cont)
    return quantidade