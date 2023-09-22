def acima_da_media(lista):
    """Função que recebe um parâmetro (lista) com as notas dos alunos, e calcula a média
    da turma e retorna a lista das notas acima da média.
    list -> list"""
    
    media_turma = sum(lista)/len(lista)
    
    list.append(lista,media_turma)
    list.sort(lista)
    
    lista_unica = list(set(lista))
    indice_media = list.index(lista_unica,media_turma)
    
    del lista_unica[0:indice_media]
    
    list.remove(lista_unica,media_turma)

    return lista_unica