def acima_da_media (lista_notas) :
    """Funcao que recebe uma lista com a nota dos alunos e retorna uma lista ordenada com as notas que ficaram acima da media"""
    media = sum(lista_notas)/len(lista_notas)
    lista_notas_acima_da_media = []
    for x in lista_notas:
        if x > media :
            list.append(lista_notas_acima_da_media, x)
            list.sort(lista_notas_acima_da_media)
            return lista_notas_acima_da_media