def fatorial(numero):
    '''Fatora um numero;
    int -> int'''
    fator = 1
    resto = numero
    fatorial = 1
    while resto != 1:
        if numero%fator == 0: 
           resto = resto/fator
           fatorial = fatoria * fator
           fator = fator + 1
        else:
             fator = fator + 1

    return  fatorial