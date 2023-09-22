def primo(numero):
    """funcao que, dado um numero inteiro positivo, verifica se o valor de entrada e um numero primo;
    int -> bool"""
    divisores=0
    for n in range(1,numero+1,2):
        if numero%2==0 or numero==2:
            return False
        else:
    return divisores==2