def acima_da_media(lista):
    """função que dada uma lista com as notas dos alunos de uma turma retorna uma lista ordenada com as notas acima da média;
    list-> list"""
    var1 = sum(lista)/len(lista)
    list.append(lista,var1)
    list.sort(lista)
    return lista[var1+1: ]