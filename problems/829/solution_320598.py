def soma_h(n):
    ''' usando o rangue para retornar uma lista, usando o n+1
    para acrescentar '''
    lista=list(range(1,n+1))
    soma=0
    for i in lista:
        soma+=1/i
    return round(soma,2)