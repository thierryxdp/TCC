def primo(numero):
    """ A função recebe um número inteiro positivo, e deve
    verificar se este número é primo ou não. Retornando o
    valor booleano 'True' caso o número se confirme como
    primo, e 'Falso' no contrário."""
    
    primou=0
    sera=range(2,numero+1)
    for num in sera:
        menor= (num<numero)
        iguaior= (num>=2)
        num>1 and num%1==0 and num/numero ==0:
        if numero%(menor) ==0 or numero%(iguaior) ==0:
            primou=False
        else:
            primou=True
    return primou