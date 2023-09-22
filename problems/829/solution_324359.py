def soma_h(n):
    ''' Essa função calcula o valor de h;int->float'''
    lista=[]
    for numero in range(1,n+1):
        h=1/numero
        lista.append(h)
    return round(sum(lista),2)