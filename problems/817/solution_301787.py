def acima_da_media(list):
    '''função em que dada uma lista com as notas dos alunos
    de uma turma, retorne uma lista ordenada com as notas
    que ficaram acima da média; list -> list'''
    media=sum(lista)/len(lista)
    mensagem= melhores(lista,media)
    return mensagem