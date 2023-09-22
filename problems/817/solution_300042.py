def acima_da_media(lista_de_notas):
    """Funçao que faz a media das notas dos alunos"""
    "list-->list"
    import math
    media = math.floor(sum(lista_de_notas)/len(lista_de_notas))
    
    list.append(lista_de_notas, media)
    list.index(lista_de_notas, media)
    list.sort(lista_de_notas)
    return lista_de_notas[media: ]