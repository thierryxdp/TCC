def qtd_divisores(numero):
    """A funcao qtd_divisores recebe um numero inteiro qualquer e devolve o numero de divisores
    do mesmo.
    entrada: int
    saida: int"""
    divisores = 0
    for indice in range(1,numero + 1):
        if numero%indice == 0:
           divisores = divisores + len([indice])
    return divisores