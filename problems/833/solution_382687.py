def conta_numero(numero,matriz):
    """
    Função que recebe uma matriz e um número inteiro e retorna
    a quantidade de ocorrências desse número na matriz.
    
    int, list --> int
    """
    n=0
    for linha in matriz:
        for elemento in linha:
            if elemento==numero:
                n+=1
    return n