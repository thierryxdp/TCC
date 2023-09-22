def soma_h(n):
    '''retorna a soma de h,onde h é 1+1/2+...+1/n,int->float'''
    lista=[]
    i=1
    for num in range(1,n+1):
        if i<=n:
            lista.append(1/i)
            i=i+1
            
    return round(sum(lista),2)