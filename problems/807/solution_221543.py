def conta_frases(a):
    '''dada uma string, é informado quantas frases tem nela
       str -> int'''
    a=str.count(a,'.')
    c=str.count(a,'?')
    d=str.count(a,'...')
    
    return a+b+c+d