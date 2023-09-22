def maiores(lista,n):
    """Pede uma lista de números inteiros e um número inteiro n.
    Retorna uma lista que contenha os numeros da lista original
    maiores que n
    list,int->list"""
    nova_lista=[]
    for m in range(len(lista)):
        if lista[m]>n:
            nova_lista=nova_lista+[lista[m]]
    return nova_lista.sort()