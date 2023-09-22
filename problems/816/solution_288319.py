def maiores(lista,n):
    ''' funcao que dada uma lista de numeros inteiros e umnumero n retorna todos os numers maiores q n
    list,int >>> list'''
    nova_lista=[]
    tamanho= len(lista)
    while tamanho > 0:
        if lista[0] > n:
            nova_lista.extend(lista[0])
            lista.remove(lista[0])
    nova_lista.sort()
    return nova_lista