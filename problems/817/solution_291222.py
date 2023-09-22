def acima_da_media(notas):
    '''Retorna a média da turma e uma
       lista com as notas que ficaram
       acima da média;list->int,list'''
    media=sum(notas)/len(notas)
    notas_=notas
    notas_+=[media]
    notas_.sort()
    maiores=list.index(notas_,media)
    turma=notas_[maiores+1:]
    list.sort(turma)
    return media,turma