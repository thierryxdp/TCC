def primo(numero):
    """ A função recebe um número inteiro positivo, e deve
    verificar se este número é primo ou não. Retornando o
    valor booleano 'True' caso o número se confirme como
    primo, e 'Falso' no contrário."""
    
    primou=False
    sera=range(2,numero+1)
    for num in sera:
        if numero%2 ==0 or numero%3 ==0:
            primou=True
    return primou