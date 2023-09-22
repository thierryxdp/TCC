def maiores(numeros,n):
    """retorna uma nova lista com todos os numeros maiores que n presentes na lista passada;
    list,int -> list"""
    lista=list.append(numeros,n)
    lista=list.sort(numeros)
    indice_n=list.index(lista,n)
    return lista[indice_n+1:]