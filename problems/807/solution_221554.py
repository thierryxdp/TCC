def conta_frases(a):
    '''dada uma string, é informado quantas frases tem nela
       str -> int'''
    a=str.count('.')
    b=str.count('...')
    c=str.count('!')
    d=str.count('?')
    
    return a-2b+c+d