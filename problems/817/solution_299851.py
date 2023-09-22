def acima_da_media (notas):
    '''
    função que dada uma lista com a nota dos alunos de uma turma,
    retorne uma lista com as notas acima da média
    list--->list
    '''
    media= sum(notas)/len(notas)
    passo1=list.append(notas,media)
    passo2=list.sort(notas)
    posicao= list.index(notas,media)
    del(notas[:posicao+1])

    return notas