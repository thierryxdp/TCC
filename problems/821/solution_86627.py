def fatorial(numero):
    '''calcula o fatorial desse numero.int->int'''
    i=numero-1
    j=numero
    resultado=j*i
    while i>1:
        j=j-1
        i=i-1
        resultado=resultado*j*i