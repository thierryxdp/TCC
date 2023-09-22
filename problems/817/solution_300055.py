def acima_da_media(lista_de_notas):
    """Funçao que faz a media das notas dos alunos"""
    "list-->list"
    import math
    
    if media > len(lista_de_notas):
        media = sum(lista_de_notas)//len(lista_de_notas)
        list.sort(lista_de_notas)
        return lista_de_notas[media: ]