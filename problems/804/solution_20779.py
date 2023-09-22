def filtra_pares(x):
    'Função que checa e retorna valores pares, dada uma tupla.'
    'tupla -> tupla'
    xt = ()
    if x[0]%2 == 0:
        xt = xt + (x[0],)
    if x[1]%2 == 0:
        xt = xt + (x[1],)
    if x[2]%2 == 0:
        xt = xt + (x[2],)
    if x[3]%2 == 0:
        xt = xt + (x[3],)
    return xt