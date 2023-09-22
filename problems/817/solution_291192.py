def acima_da_media(lista):
    """Dada uma lista de notas, esse função retorna uma lista ordenada das notas que ficaram acima da média dessas mesmas notas; list -> list"""
    media = sum(lista)/len(lista)
    list.sort(lista)
    
    lista_ordenada = [i for i in lista if i > media]
    
    return lista_ordenada