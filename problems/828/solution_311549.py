def primo(n):
    '''Função que dado um número inteiro positivo, verifique se este número é
       primo ou não, retorne um valor booleano.
       int ---> bool'''
    inicio = 1
    divisor = 0
    while inicio <= n:
        if n % inicio ==0:
            divisor = divisor + 1
        inicio = inicio + 1
    if divisor > 2:
        return False
    else:
        return True