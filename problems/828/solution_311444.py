def primo(n):
    '''função que dado um número 'n' inteiro positivo, verifica se este
       número é primo ou n˜ao e retorna um valor booleano.
       int->bool '''
    contador=0
    for c in range(1,n+1):
        if n%c==0:
            contador=contador+1
    if contador==2:
        return True
    else:
        return False