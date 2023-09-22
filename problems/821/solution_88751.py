def fatorial(numero):
    'dado um numero, retorna o fatorial desse numero'
    contador=1
    fatorial=1
    if numero==0 or numero==1:
        return 1
    while numero >= contador:
        fatorial = fatorial * contador
        contador+=1
    return fatorial