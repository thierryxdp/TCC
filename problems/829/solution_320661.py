def soma_h(N):
    lista=[]
    for x in range(1,N+1):
        lista.append((1/x))
    return round(sum(lista),2)