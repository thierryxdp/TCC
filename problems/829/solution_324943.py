def soma_h(x):
    """Dada uma funcao que calcula e retorna o valor H com N termos onde N e inteiro.
    Entrada: int,float"""
    r = 1
    for i in range(2, x+1):
        if x>0:
            r = r + 1/i
    return round(r, 2)