def fatorial(n):
    """ função que calcula o fatorial dado um numero
        Entrada --->
        Saida   ---> """
    m = 1
    while n >= 1:
        m = m * n
        n = n - 1
    return m


""" Teste:
    Respostas Esperadadas
    1 -> 1
    2 -> 2
    3 -> 6
    4 -> 24 
    5 -> 120
    6 -> 720
    7 -> 5040
    Resultados Obtidos:
    >>> fatorial(1)
     1
    >>> fatorial(2)
     2
    >>> fatorial(3)
     6
    >>> fatorial(4)
     24
    >>> fatorial(5)
     120
    >>> fatorial(6)
     720
    >>> fatorial(7)
     5040
    """