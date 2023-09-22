def filtraMultiplos(lista,n):
    '''funcao que retorna os numeros de uma lista que sejam divisiveis por n'''
    resp=[]
    i=0
    while i<=len(lista):
        if (lista[i]%n)==0:
            resp.append(lista[i])
            i+=1
    return resp