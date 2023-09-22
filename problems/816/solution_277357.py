def maiores(lista,n):
    """Analisa todos os números contidos na lista maiores que n. Retorna
    outra lista contendo apenas esses números.
    list,int -> list"""
    if n in lista==True:
        lista
    else:
        list.append(lista,n)
    
    list.sort(lista)
    v=' '
    list.append(v,lista[list.index(lista,n)+1:])
    return v