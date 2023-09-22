def primo(numero):
    """ A função recebe um número inteiro positivo, e deve
    verificar se este número é primo ou não. Retornando o
    valor booleano 'True' caso o número se confirme como
    primo, e 'Falso' no contrário."""
    
    primou=False
    for num in range(1,numero+1):
        if num%2 ==0 or num%3 ==0:
            primou=True
    return numero