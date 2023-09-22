def acima_da_media(lista_notas):
    """Funcao que dada uma lista com a nota dos alunos, retorna uma lista ordenada
com as notas acima da media"""
    media = (sum(lista_notas)//len(lista_notas))
    if media in lista_notas:
        list.sort(lista_notas)
        indexa = list.index(lista_notas,media)
        return lista_notas[indexa+1:]
    else:
        list.append(lista_notas,media)
        list.sort(lista_notas)
        indexa = list.index(lista_notas,media)
        return lista_notas[indexa+1:]