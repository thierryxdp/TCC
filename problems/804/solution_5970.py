def filtra_pares(a, b, c, d):
    '''Função que recebe uma tupla com quatro números inteiros como parâmetro
    e retorna uma nova tupla contendo apenas os elementos pares da tupla original
    na mesma ordem em que se encontravam.
    tupla(int,int,int) -> tupla(int,int,int,int)'''
    a_par = a%2 == 0
    b_par = b%2 == 0
    c_par = c%2 == 0
    d_par = d%2 == 0
    
    if a_par and b_par and c_par and d_par:
        return a, b, c, d
    if a_par and b_par and c_par:
        return a, b, c
    if a_par and b_par and d_par:
        return a, b, d
    if a_par and c_par and d_par:
        return a, c, d
    if b_par and c_par and d_par:
        return b, c, d
    if a_par and b_par:
        return a, b
    if a_par and c_par:
        return a, c
    if a_par and d_par:
        return a, d
    if b_par and c_par:
        return b, c
    if b_par and d_par:
        return b, d
    if c_par and d_par:
        return c, d
    if a_par:
        return a
    if b_par:
        return b
    if c_par:
        return c
    if d_par:
        return d
    else:
        return 'nenhum número é par.'