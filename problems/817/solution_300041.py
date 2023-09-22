def acima_da_media(lista_de_notas):
    """Funçao que faz a media das notas dos alunos"""
    "list-->list"
    media = 5
    A = list.sort(lista_de_notas)
    
    if lista_de_notas[1] == None:
        return []
    if  lista_de_notas[1] != None and 5 in lista_de_notas :
        list.sort(lista_de_notas)
        A=list.index(lista_de_notas, 5)
        return lista_de_notas[A: ]

    elif lista_de_notas[1] != None and 5 not in lista_de_notas :
        list.append(lista_de_notas, 5)
        list.sort(lista_de_notas)
        A=list.index(lista_de_notas, 5)
        list.pop(lista_de_notas, A)

        return lista_de_notas[A: ]