def acima_da_media(notas):
    '''A funcao recebe uma lista de notas de uma turma e retorna as notas que estao
acima da media geral da turma list->list'''
    n=(sum(notas)/len(notas))
    notas.append(n)
    notas.sort()
    return maiores(notas,n)