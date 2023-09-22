def conta_numero(numero,matriz):
    ''''''
    lista=[]
    for n in range(len (matriz)):
        if numero in matriz[n]:
            c=list.count(matriz[n],numero)
            list.append(lista,c)
    return sum(lista)