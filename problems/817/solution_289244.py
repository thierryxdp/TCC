def acima_da_media(lista):
    """função que dada uma lista com as notas dos alunos de uma turma retorna uma lista ordenada com as notas acima da média;
    list-> list"""
    var1 = sum(lista)/len(lista)
    if var1 in lista:
        var2 = list.index(var1)
        return lista[var2+1:]
    else:
        list.append(lista,var1)
        list.sort(lista)
        var3 = list.index(lista,var1)
        return lista[var3+1:]