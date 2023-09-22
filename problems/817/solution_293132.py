def acima_da_media(notas):
    '''Função que dada uma lista de notas de alunos (notas)
    retorna quais notas ficaram acima da média em uma lista 
    ordenada.
    list([float])-> list([float])'''

    soma_notas= sum(notas)
    media= soma_notas/(len(notas))
    list.append(notas,media)
    list.sort(notas)
    posicao=list.index(notas,media)
    x=list.count(notas,media)
    acima_media=notas[posicao+x:]

    return acima_media