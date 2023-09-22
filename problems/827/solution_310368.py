def qtd_divisores(n):
    '''Recebe um número e quantifica seus divisores;
    int -> int'''
    d = 1 
    qtd = 0
    while d <= n:
        if n%d == 0:
            qtd = qtd + 1
        d = d + 1
            
    return qtd