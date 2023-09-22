def conta_numero(numero, matriz):
    lista=0
    f=str(matriz)
    k=f.replace('[','')
    m=k.replace(']','')
    g=m.replace(' ','')
    z=g.replace(',','') #voltaria uma string
    for i in z:
        if i== str(numero):
            lista+=1
    return lista