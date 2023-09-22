def fatorial(n,contador):
    '''funcao que calcula o fatorial de um numero recebido.int ->int'''
    fatorial = 1 
    contador=n-1
    while (n > 0):
        fatorial = n *(contador) 
        contador = n - 1 
    else:
            return fatorial
        if n< 0:
            fatorial = 'indefinido'
            return fatorial