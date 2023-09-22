def primo(n):
    
    """Função que recebe um númer n inteiro e positivo e verifica se o número é primo
    int ->  boolean
    """
    p = int(n/2)    
    re = True
    while re and p > 1:
        if  n%p == 0:
            re = False
        p = p -1
    return re