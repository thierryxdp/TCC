def filtraMultiplos(lista,n):
    '''funcao que retorna os numeros de uma lista que sejam divisiveis por n'''
    resp=[]
    proximo=0
    i=proximo
    while i<=len(lista):
        if (lista[i]//n)==0:
            resp.append(lista[i])
            i=proximo+1