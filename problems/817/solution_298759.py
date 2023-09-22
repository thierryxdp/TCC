def acima_da_media(notas):
    """retorna uma nova lista com todos os numeros maiores que n presentes na lista passada;
    list,int -> list"""
    
    media=int(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    i=list.index(notas,media)
    return notas[i+1:]