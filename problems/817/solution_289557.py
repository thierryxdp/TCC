def acima_da_media(lista_notas):
    """Função que dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que 
    ficaram acima da média
    list -> list"""
    media = sum(lista_notas)/len(lista_notas)
    list.append(lista_notas, media)
    list.sort(lista_notas)
    del lista_notas[0:list.index(lista_notas, media)+1]
    return lista_notas