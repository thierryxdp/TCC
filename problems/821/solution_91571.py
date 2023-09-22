def fatorial(n):
    '''Função calcula o fatorial de um número n. int -> int'''
   
    x=1
    f=1
    while x<=n:
        f=f*x
        x=x+1
       
    return f