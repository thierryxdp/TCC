def soma_h(n):
    lista=range(1,n+1)
    soma=[]
    for i in lista:
        soma.append(1/i)
    return round(sum(soma),2)