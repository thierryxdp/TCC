def primo(numero):
    '''
    verifica se o numero em questao e primo ou nao
    int -> bool
    '''
    quantidade_divisores=0
    for num in range(1,numero+1):
        if numero%num==0:
            quantidade_divisores=quantidade_divisores+1
        if quantidade_divisores=2:
            return True
        else:
            return False