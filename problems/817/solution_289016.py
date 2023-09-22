def acima_da_media(notas):
    "função que dada uma lista com notas dos alunos de uma turma, retorna a média da turma e uma lista ordenada com as notas que ficaram acima da média."
    media = sum(notas) / len(notas)
    lista = notas + [media]
    list.sort(lista)
    p_partida = list.index(lista,media)
    quantidade = list.count(lista,media)
    return lista[p_partida + quantidade:]