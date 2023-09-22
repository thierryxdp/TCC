def filtraMultiplos(lista_num,n):
    """retorna uma lista contendo os elementos de lista_num que forem divisiveis por n;
    list,int -> list"""
    i=0
    divisiveis=[]
    
    while i<len(lista_num):
        if lista_num[i]%n==0:
            list.append(divisiveis,lista_num[i])
        i=i+1
    return divisiveis