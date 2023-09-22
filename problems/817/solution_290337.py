def acima_da_media(lista_com_medias):
    """dada uma lista com as notas dos alunos da turma, retorne as notas ordenadas que ficaram acima da media"""
    a=len(lista_com_medias)
    b= (sum(lista_com_numeros))/a
    list.append(lista_com_medias,b)
    list.sort(lista_com_medias)
    posicao= list.index(lista_com_medias,b)+1
    return lista_com_medias[posicao:]