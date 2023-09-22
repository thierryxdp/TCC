def primo(n):
    '''Dado um numero inteiro positivo, verifica se este numero e primo ou nao. 
    Retorna um valor booleano
    int -> bool'''
    for i in (1.5,n+1):
        if i>n%i==0:
            return False
        else:
            return True