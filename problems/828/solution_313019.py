def primo(n):
    '''Dado um numero inteiro positivo, verifica se este numero e primo ou nao. 
    Retorna um valor booleano
    int -> bool'''
    for i in (1,n+1):
        if i>1:
            if i%n==0:
                return False