def primo(numero):
    '''funçao que dado um numero inteiro positivo, verifica
    se este numero é primo ou nao. Retorna um valor booleado;
    int -> bool'''
    divisores = []
    for i in range(numero+1):
        if numero%(i+1)==0:
            divisores += [i+1,]
    return len(divisores)==2