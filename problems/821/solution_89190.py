def fatorial(n=1, show=False):
    """ => Calcula o fatorial de um número.
        :param n: O número a ser calculado
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do fatorial de um número n."""
    
    m = 1
    conta = f''
    for c in range(n, 0, -1):
        m *= c
        if c > 1:
            conta += f'{c} X '
        elif c == 1:
            conta += f'{c}'
    if show == True:
        return f'{conta} = {m}'
    else:
        return m