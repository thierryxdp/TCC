def fatorial(numero):
    lista=[]
    contador=numero
    while contador>0:
        lista.append(contador)
        contador-=1
    produto = reduce(mul, lista, 1)
    return produto