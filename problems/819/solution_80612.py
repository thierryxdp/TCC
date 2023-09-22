def filtraMultiplos(lista,n):
    """retorna outra lista contendo todos os elementos da lista original que forem divisiveis por n; list, float ->list"""
    a=0
    b=[]
    while a<len(lista):
        if n%lista[a]!=0:
            list.append(b,a)
        a=a+1
    return b