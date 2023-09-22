def acima_da_media(lista_notas):
    """ Dada uma lista com as notas dos alunos de uma turma retorna uma
    lista ordenada com as notas que ficaram acima da média. 
    list -> list"""
    import math
    media = int(math.floor(sum(lista_notas)/len(lista_notas)))
    if media in lista_notas:
        list.append(lista_notas, media)
        list.sort(lista_notas)
        ocorrencia = list.index(lista_notas, media)
        return lista_notas[ocorrencia+2:]
    else:
        list.append(lista_notas, media)
        list.sort(lista_notas)
        ocorrencia = list.index(lista_notas, media)