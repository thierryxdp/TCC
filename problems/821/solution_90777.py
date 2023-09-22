def fatorial(numero):
    '''Calcula o fatorial do numero dado;
    int->int'''
    
    ultimo_numero=numero+1
    lista=list(range(1,ultimo_numero))
    fatorial=1
    i=0
    
    while i<len(lista):
        fatorial=fatorial*lista[i]
        i+=1
    return fatorial