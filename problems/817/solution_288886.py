def acima_da_media(notas):
    '''Retorna quais notas ficaram acima da média da turma;
    list -> list'''
    media=sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    local=list.index(notas,media)
    return notas[local+list.count(notas,media):]