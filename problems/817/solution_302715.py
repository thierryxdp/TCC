def acima_da_media(notas):
    '''função chamada acima_da_media que dada uma lista com as
    notas dos alunos de uma turma, retorna uma lista 
    ordenada com as notas que ficaram acima da média.
    list,int->list'''
    total=len(notas)
    soma=sum(notas)
    media=soma/total
    list.append(notas,media)
    list.sort(notas)
    eliminar=list.index(notas,media)
    eliminado=eliminar+2
    maioresN=notas[eliminado:]
    return maioresN