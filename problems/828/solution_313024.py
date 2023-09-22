def primo(n):
    '''Dado um numero inteiro positivo, verifica se este numero e primo ou nao. 
    Retorna um valor booleano
    int -> bool'''
    i=2
    while i in (1,n+1):
        if (n+1)%i==0:
            i=i+1
            return False