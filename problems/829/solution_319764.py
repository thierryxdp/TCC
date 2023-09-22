def soma_h(n):
    '''soma_h recebe um numero inteiro n e retorna o valor de H.
    Sendo H=(1+1/2+1/3+...+1/n).
    Assume n numero inteiro.
    int-->float.'''
    H=0
    valores=range(n+1)
    for numero in valores:
        H=H+(1/n)
    return round(H,2)