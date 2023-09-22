def acima_da_media(lista):
    """Essa funcao recebe uma lista com todas as notas dos alunos e retorna uma lista com todas as notas que
    ficaram acima da media;
    list -> list
    """
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    nova_lista = lista[list.index(lista,media)+1:]
    if type(nova_lista[0]) == float:
        return nova_lista[1:]
    else:
        return nova_lista