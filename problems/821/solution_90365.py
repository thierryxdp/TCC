def fatorial(n):
    lista=[]
    resultado = n
    i=1
    while n>=1:
        lista.append(n)
        n = n-1
    while i<len(lista):
        resultado = resultado * lista[i]
        i += 1
    return resultado