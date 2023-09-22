def filtraMultiplos(lista,n):
    """retorna uma lista contendo tos os elemetos da lista original que forem divisíveis por n.
    list,int->list"""
    d=[]
    prox=0
    
    while prox<len(lista):
        if lista[prox]%n==0:
            d=d+(lista[prox],)
        prox=prox+1
    return d