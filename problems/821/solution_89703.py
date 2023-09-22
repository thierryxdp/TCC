def fatorial(numero):
    fatorial=numero
    termo=numero-1
    while termo>=1:
        fatorial=fatorial*termo
        termo= termo -1
    return fatorial