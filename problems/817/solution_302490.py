def acima_da_media(lista_notas):
    '''dada a lista com as notas dos alunos, retorna outra lista com as notas acima da media; list -> list'''
    return maiores_que(lista_notas,(sum(lista_notas))/(len(lista_notas)))