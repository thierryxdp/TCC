def acima_da_media(lista_de_notas):
    """Funçao que faz a media das notas dos alunos"""
    "list-->list"
    media = 5
    A = list.sort(lista_de_notas)
    base = lista_de_notas[0] + lista_de_notas[1]
    
    if   base < 1 and 5 in lista_de_notas :
        list.sort(lista_de_notas)
        A=list.index(lista_de_notas, 5)
        return lista_de_notas[A: ]

    elif base < 1 and 5 not in lista_de_notas :
        list.append(lista_de_notas, 5)
        list.sort(lista_de_notas)
        A=list.index(lista_de_notas, 5)
        list.pop(lista_de_notas, A)

        return lista_de_notas[A: ]

    else:
        return []