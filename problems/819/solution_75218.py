def filtaMultiplos(lista,n):
    lista=[]
    numero=0
    while numero<len(n):
        if lista[numero]%n==0:
            lista=lista+(lista[numero],)
        numero=numero+1
    return lista