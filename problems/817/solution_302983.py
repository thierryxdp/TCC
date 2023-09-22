def acima_da_media(lista):
    """lista -> lista;
    Função que, dada uma lista com as notas dos alunos de uma
    turma, retorna uma lista ordenada com as notas que estão
    acima da média."""
    n = sum(lista)/len(lista)
    ret = []
    for e in l:
        if e > n:
            list.append(ret, e)
    list.sort(ret)
    return ret