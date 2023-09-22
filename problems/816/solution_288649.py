def maiores(lista,n):
    i=0
    resposta=[]
    for i in lista:
        if n<lista[i]:
            resposta=lista[i]
        i=i+1
    return resposta