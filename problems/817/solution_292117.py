def acima_da_media(lista_nota):
    """
    list->list
    :param lista_nota: Recebe lista com as notas de todos os alunos de uma turma
    return: Retorna lista ordenada dos alunos que tiveram nota acima da média
    """
    media = sum(lista_nota)/(len(lista_nota)) #calcula a media
    lista_maior_nota = maiores_que(lista_nota, media) 
    return media, lista_maior_nota;