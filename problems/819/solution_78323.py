def filtraMultiplos(lista,n):
    """Funcao calcula e retorna uma lista com elementos da lista original que forem divisivel por um numero(n);
    list,int->list"""
    multiplos=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            multiplos.append(lista[i])
        i=i+1
    return multiplos