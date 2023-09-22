#Start your python function here
def filtra_pares(tupla):
    """ Recebe uma tupla com quatro elementos inteiros como parâmetro, e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam.
        
        Parameters:
            tupla = tupla com quatro elementos
        
        Testes:
            filtra_pares((1,2,3,4)) = (2,4)
            filtra_pares((2,4,6,8)) = (2,4,6,8)
            filtra_pares((1,3,5,7)) = ()

        Returns:
            Tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam.
            tuple -> tuple.
    """
    a, b, c, d = tupla
    resultado = 0,
    if  a % 2 == 0:
        a = (a,)
        resultado = resultado + a
    if  b % 2 == 0:
        b = (b,)
        resultado = resultado + b
    if  c % 2 == 0:
        c = (c,)
        resultado = resultado + c
    if  d % 2 == 0:
            d = (d,)
            resultado = resultado + d
    return resultado [1:]