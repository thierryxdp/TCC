def primo(n):
    '''Dado um numero inteiro positivo, verifica se este numero e primo ou nao. 
    Retorna um valor booleano
    int -> bool'''
    for i in (2,n+1):
        if (n+1)%i==0:
            return False
        else:
            return True