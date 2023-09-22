def conta_frases(a):
    '''dada uma string, é informado quantas frases tem nela
       str -> int'''
    a=str.replace(a,'...','/')
    a=str.replace(a,'.','/')
    a=str.replace(a,'?','/')
    a=str.replace(a,'!','/')
    
    return str.count(a,'/')