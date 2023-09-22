def melhor_volta(matriz):
    lista=[]
    menor=[]
    minimo=0
    c_linha=0
    c_coluna=0
    lista1=[]
    i=0
    for lista in matriz[i]:
        if 0<=i<=10:
            lista1+=[min(lista)]
        i+=1
    return min(lista1)
    #for e in matriz[i]:
    #    if i==
    #    c_linha+=1
    #list.append(menor,min(matriz[i]))