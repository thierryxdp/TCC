def fatorial(numero):
    i=0
    while i<=numero:
        numero+=numero
        x=numero*(numero-1)
        i=i+1
    return x