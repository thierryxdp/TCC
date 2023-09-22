def maiores(lista,n):
    ''' funcao que dada uma lista de numeros inteiros e umnumero n retorna todos os numers maiores q n
    list,int >>> list'''
    nova_lista=[]
    
    while len(lista) > 0:
        if lista[0] > n:
            nova_lista.append(lista[0])
            lista.remove(lista[0])
        if len(lista)==0:
            return nova_lista
        if lista[0]< n:
            lista.remove(lista[0])
    nova_lista.sort()
    return nova_lista