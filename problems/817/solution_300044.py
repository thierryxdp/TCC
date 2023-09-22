def acima_da_media(lista_de_notas):
    """Funçao que faz a media das notas dos alunos"""
    "list-->list"
    import math
    media = (sum(lista_de_notas)//len(lista_de_notas))
    
    if media in lista_de_notas:
        list.index(lista_de_notas, media)
        list.sort(lista_de_notas)
        return lista_de_notas[media: ]