def acima_da_media(lista):
    '''funç̃ao que dada uma lista com as notas dos alunos de uma turma,
    retorne uma lista ordenada com as notas que ficaram acima da média.
    lista->lista '''
    soma_termos=sum(lista)
    termos=len(lista)
    media=soma_termos//termos
    x=maiores(lista,media+1)
    return x