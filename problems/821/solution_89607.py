def fatorial(n):
    '''funcao que dado um numero, retorna o fatorial dele;
    int->int'''
    i=n
    multiplicacao= 1
    while i>0:
        multiplicacao= multiplicacao* i*(i-1)
        i = i-2
        
    return multiplicacao