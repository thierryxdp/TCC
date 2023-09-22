def acima_da_media(notas):
    "função que dada uma lista com notas dos alunos de uma turma, retorna a média da turma e uma lista ordenada com as notas que ficaram acima da média."
    media = sum(lista)/float(len(lista))
    list.apped(lista,media)
    list.sort(lista)
    posicao = list.index(lista,media)
    lista1 = lista[posicao+1:]
    del lista[0:posicao+1]
    if media in lista:
        posicao = list.index(lista,media)
        del lista[posicao]
        return (media,lista)