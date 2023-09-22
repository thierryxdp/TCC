def faltante(l):
    '''dada uma lista com N-1 int numerados de 1 a N
    retorna qual num inteiro deste intervalo esta faltando
    list -> int'''
    
    l.sort()
    i=1
    
    while i in l:
        i=i+1
        
    return i