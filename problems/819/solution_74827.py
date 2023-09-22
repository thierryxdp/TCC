def filtraMultiplos(lista,n):
    """ Funcao recebe uma lista e um numero e retorna outra lista com todos os elementos da lista original que forem divisiveis por n
    list,int->list"""
    lista2=[]
    x=0
    while x<=len(lista)-1:
        if lista[x]%n==0:
            lista2.append(lista[x])
        x=x+1
    return lista2