def acima_da_media(lista_notas):
    
    media = sum(lista_notas) / len(lista_notas)
    
    list.insert(lista_notas,0,media+1)
    list.sort(lista_notas)
    
    posicao = list.index(lista_notas,media)
    
    return lista_notas[posicao+1:]