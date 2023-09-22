def media(notas):
    '''função que dado uma lista com notas dos alunos de uma turma, retorna a média
    da turma e uma lista ordenada com as notas que ficaram acima da média.
    list -> list'''
    m = sum(notas) / len(notas)
    lista = notas + [m]
    list.sort(lista)
    a = list.index(lista,m)
    b = list.count(lista,m)
    return m, lista[a + b:]