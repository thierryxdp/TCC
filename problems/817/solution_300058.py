def acima_da_media(lista_de_notas):
    """Funçao que faz a media das notas dos alunos"""
    "list-->list"
    import math
    media = sum(lista_de_notas)/len(lista_de_notas)
    A = len(lista_de_notas)//2
    m = math.floor(media)
    M = m//2

    if len(lista_de_notas) == 1:
        return []

    elif len(lista_de_notas) == 2:
        return max(lista_de_notas)

    elif media > len(lista_de_notas)/2 and len(lista_de_notas) > 2:
        list.sort(lista_de_notas)
        return lista_de_notas[M: ]

    elif media < len(lista_de_notas)/2 and len(lista_de_notas) > 2:
        list.sort(lista_de_notas)
        
        return lista_de_notas[A: ]