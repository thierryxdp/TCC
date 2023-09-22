def acima_da_media(lista):
    "função que dada uma lista com notas dos alunos de uma turma, retorna a média da turma e uma lista ordenada com as notas que ficaram acima da média."
    media1 = sum(lista)/float(len(lista))
    list.append(lista,media1)
    list.sort(lista)
    posicao = list.index(lista,media1)
    lista1 = lista[posicao+1:]
    del lista[0:posicao+1]
    if media1 in lista:
        posicao = list.index(lista,media1)
        del lista[posicao]
        return (media1,lista)