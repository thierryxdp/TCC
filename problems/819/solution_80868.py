def filtraMultiplos(lista_num,n):
    """retorna uma lista contendo os elementos de lista_num que forem divisiveis por n;
    list,int -> list"""
    i=0
    lista=[]
    
    while i<len(lista_num):
        if lista_num[i]%n==0:
            list.append(lista_num,lista_num[i])
        i=i+1
    return lista