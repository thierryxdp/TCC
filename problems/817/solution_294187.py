def maiores(lista,n):
    if n not in lista_num:
        list.append(lista_num,n)
    list.sort(lista_num)
    indice= list.index(lista,n)

    fatiado= lista[indice+1:]
    return fatiado

def acima_da_media(lista):
    '''Faça uma função acima da media que dada uma lista com as notas dos alunos de uma turma, retorne
uma lista ordenada com as notas que ficaram acima da média; list ->list.'''
    media= sum(lista)/len(lista
    return maiores(lista,media)