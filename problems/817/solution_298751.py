def acima_da_media(notas):
    """retorna uma nova lista com todos os numeros maiores que n presentes na lista passada;
    list,int -> list"""
    
    lista=list.append(notas,7)
    lista=list.sort(notas)
    indice=list.index(lista,7)
    return lista[indice+1:]