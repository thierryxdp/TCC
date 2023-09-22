def soma_H (n):

    """funcao que retorna a soma de 1 + 1/n termos"""
    #int -> float

    h = 0

    for i in range (1, n+1):
        j = 1/i
        h += j

    return h