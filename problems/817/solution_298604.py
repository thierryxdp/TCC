def acima_da_media(notas):
    """ Insira as notas dos alunos dessa turma e a funcao retornara uma lista ordenada 
    com as notas que ficaram acima da media"""
    media = sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    list.reverse(notas)
    m = list.index(notas,media)
    lista = notas[0:m]
    list.sort(lista)
    return lista