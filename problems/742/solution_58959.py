def substitui(s,x,i):
    '''Função que retorna uma string que substituí um elemento da posição i por um caractere'''
    w = list(s)
    w[i] = x
    alterado = "".join(w)
    return alterado