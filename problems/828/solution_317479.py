def primo(n):
    '''Função que dado um número(n) inteiro e positivo, verifica se ele é primo ou não;
       int->bool'''
    d = 0
    for j in range(1,n+1):
        if n%j==0:
            d=d+1
    elif d==2:
        return True
    else:
        return False