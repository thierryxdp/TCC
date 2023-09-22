def fatorial(n):
    '''Função que calcula o fatorial de um número passado como
    	parêmetro
        
        int -> int'''
    a=1
    f=0
    while (n-f)!=1:
        a=a*(n-f)
        f=f+1
    return a