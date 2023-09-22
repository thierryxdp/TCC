def melhor_volta(matriz):
    a=min(matriz[0])
    b=min(matriz[1])
    c=min(matriz[2])
    d=min(matriz[3])
    e=min(matriz[4])
    f=min(matriz[5])
    lista=[a,b,c,d,e,f]
    if min(lista) in matriz[i]:
        return i