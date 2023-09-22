def primo(n):
    '''função que, dado um número inteiro positivo, 
    verifica se este número é primo ou não.
    int -> bool'''
    tupla = ()
    for x in range(1,n+1):
        if n/x == n//x:
            tupla = tupla + (x,)
    if tupla == (1,n):
        return True
    else: 
        return False