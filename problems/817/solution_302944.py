def acima_da_media(l):
    '''Dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da média.
assinatura: list --> list'''
    m=sum(l)/len(l)
    r=[]
    for e in l:
        if e>m:
            list.append(r,e)
    list.sort(r)
    return r