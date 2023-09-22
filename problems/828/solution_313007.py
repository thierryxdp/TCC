def primo(n):
    '''Dado um numero inteiro positivo, verifica se este numero e primo ou nao. 
    Retorna um valor booleano
    int -> bool'''
    if i>1:
        for i in (1,n+1):
            if n%i==0:
                return False