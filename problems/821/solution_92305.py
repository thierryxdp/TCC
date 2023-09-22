def fatorial(n):
    produtorio = 1
    contador=0
    lista=range(1,n+1)
    while contador<len(lista):
        produtorio = produtorio*lista[contador]
        contador+=1