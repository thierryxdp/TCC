def filtraMultiplos(lista,n):
    """retorna uma lista contendo todos os elementos da lista original que forem divisíveis por n.
    list,int->list"""
    mutiplos=[]
    indice=0
    while indice<len(lista):
        if lista[indice]%n==0:
            multiplos=multiplos+lista[indice]
            indice=indice+1
        return multiplos