def qtd_divisores(numero):
    lista=[1,2,3,4,5,6,7,8,9,10]
    q=0
    for i in range(len(lista)):
        d=numero%lista[i]
        if d==0:
            q+=1
    return q