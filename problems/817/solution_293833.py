def acima_da_media(lista):
    """Funcao que retorna uma list ordenada com as notas que ficaram acima da media;
    list -> list"""
    
    list.sort(lista)
    ntermos = sum(lista)
    position = ntermos//len(lista)
   
    p = position+1
    
    
    return lista[p:]