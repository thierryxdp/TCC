def filtraMultiplos(lista,n):
    resposta=[]
    i=0
    while i<len(lista):
       if lista[i]%n==0:
        resposta+=lista[i]
       i=i+1
    return resposta