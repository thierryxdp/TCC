def fatorial(numero):
    '''função que dado um numero, calcule o fatorial desse numero;
    int-> int'''
    if numero==0:
        return 1
    else:
        fatorial=1
        while(numero>1):
            fatorial = fatorial* numero
            numero= numero-1
        return fatorial