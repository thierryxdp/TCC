def acima_da_media(lista):
    '''função em que dada uma lista com as notas dos alunos
    de uma turma, retorne uma lista ordenada com as notas
    que ficaram acima da média; list -> list'''
    media=sum(lista)/len(lista)
    mensagem= maiores(lista,media)
    return mensagem