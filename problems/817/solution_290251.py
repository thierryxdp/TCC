def acima_da_media(notas):
    '''funcao que dada uma lista com a media dos alunos de uma turma,
    retorna de forma ordenada uma nova lista com todas as notas que ficaram 
    a cima da media
    list->list'''
    media=sum(notas)/len(notas)
    list.sort(notas)
    funcao= [notas]+[media]
    funcao2= notas[:]+[media]
    list.sort(funcao2)
    ident=list.index(funcao2,media)
    contagem=list.count(funcao2,media)
    
    if contagem==1:
    	return funcao2[ident+1:]
    else:
        return funcao2[ident+contagem:]