def primo(numero):
    """Funcao que, dado um numero inteiro positivo de entrada,
    verifica se o numero e primo ou nao, retornando True se primo
    e False para nao primo;
    int -> bool"""
    divisores=[]
    for possiveis_divisores in range(1,numero,2):
        if numero%possiveis_divisores==0:
            divisores+=[possiveis_divisores]
    if len(divisores)>2:
        return False
    else:
        return True