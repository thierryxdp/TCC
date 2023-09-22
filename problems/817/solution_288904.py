def acima_da_media (lista):
    """ funcao ira receber uma lista com as notas dos alunos e retornar uma lista ordenada com as notas que ficaram acima da media da turma"""
    media = sum(lista) / len(lista)
    i = 0
    lista_nova = []
    if lista[i] >= media:
        lista_nova = lista_nova + lista[i]
        i = i + 1
    else:
        lista_nova = lista_nova
    list.sort (lista_nova)
    return lista_nova