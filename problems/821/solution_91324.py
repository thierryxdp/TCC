def fatorial(numero):
    fatorial=numero
    total=0
    while fatorial!=0:
        total+=fatorial*(fatorial-1)
        fatorial=fatorial-1
    return total