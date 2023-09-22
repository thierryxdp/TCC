def primo(n):
    '''Dado um numero inteiro positivo, verifica se este numero e primo ou nao. 
    Retorna um valor booleano
    int -> bool'''
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True