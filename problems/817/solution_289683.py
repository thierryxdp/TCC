def acima_da_media(lista_notas):
    """dada uma lista com as notas dos alunos de uma turma, a função retorna uma lista ordenada com as notas que ficaram 
    acima da da média; list -> list"""
    media = sum(lista_notas)/len(lista_notas)
    if media in lista_notas:
        list.sort(lista_notas)
        indice = list.index(lista_notas, media)
        return lista_notas[indice+1:]
    else:
        lista_notas[0:0] = [media]
        list.sort(lista_notas)
        indice = list.index(lista_notas, media)
        return lista_inteiros[indice+1:]