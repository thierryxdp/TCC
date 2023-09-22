def media(notas):
    "função que dada uma lista com notas dos alunos de uma turma, retorna a média da turma e uma lista ordenada com as notas que ficaram acima da média."
    media = sum(notas) / len(notas)
    lista = notas + [media]
    list.sort(lista)
    posiçao = list.index(lista,media)
    quantidade = list.count(lista,media)
    return media, lista[posiçao + quantidade:]