def filtraMultiplos(lista,n):
    """Função que recebe como entrada uma lista de números
    e retorna outra lista contendo todos os elementos da 
    lista original que forem divisíveis por n.
    lista,int->lista"""
    i=0
    lista2=[]
    while i<len(lista):
        if int(lista[i])%n==0:
            lista2.append(lista[i])
        i=i+1
    return lista2