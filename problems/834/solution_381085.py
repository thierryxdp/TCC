def media_matriz(matriz):
    lista=[]
    p=len(matriz)
    t=len(matriz[0])
    t=p*t
    f=str(matriz)
    k=f.replace('[','')
    m=k.replace(']','')
    g=m.replace(' ','')
    z=g.replace(',','')
    h=list(z)
    new= [int(string) for string in h]
    return round(sum(new)/t, 2)