def soma_h(n):
    lista=[]
    i=1
    for num in range(1,n+1):
        if i<=n:
            lista+=1/i
            i=i+1
    return lista