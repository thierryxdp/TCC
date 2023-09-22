def soma_h(n):
    lista=list(range(1,n+1))
    soma=[]
    for x in lista:
        soma.append(1/x)
    return round(sum(soma),2)