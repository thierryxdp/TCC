def acima_da_media(lista_notas):
    
    media = sum(lista_notas) / len(lista_notas)
    
    nova_media = media + 0.1
    
    list.insert(lista_notas,0,nova_media)
    list.sort(lista_notas)
    
    posicao = list.index(lista_notas,nova_media)
    
    return lista_notas[posicao+1:]