def soma_h(n):
    soma=0
    lista=[]
    for i in range(1,n+1):
        soma=soma+1/i
    return round(soma,2)