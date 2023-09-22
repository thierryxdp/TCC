def primo(numero):
    """ A função recebe um número inteiro positivo, e deve
    verificar se este número é primo ou não. Retornando o
    valor booleano 'True' caso o número se confirme como
    primo, e 'Falso' no contrário."""
    
    primou=0
    sera=range(2,numero+1)
    for num in sera:
        if numero%(num<numero) ==0 or numero%(num>=2) ==0:
            primou=True
        else:
            primou=False
    return primou