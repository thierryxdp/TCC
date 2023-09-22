def conta_frases(texto):
    '''
    Essa função conta o número de frases que aparecem em um determinado texto.
    Parametro de Entrada: string
    Valor de saída: int
    '''
    p1=texto.count('.')
    p2=texto.count('!')
    p3=texto.count('?')
    p4=texto.count('...')
    if  p4!=0:
        return p1-(3*p4)+p2+p3+p4
    return p1+p2+p3+p4