def acima_da_media(lista):
    '''função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da da média.
    entrada: list
    saída: list'''
    var1 = (sum(lista)/len(lista))
    if var1 in lista:
        list.sort(lista)
        var2 = list.index(lista,var1)
        return lista[var2 +1: ]
    else:
        list.append(lista,var1)
        list.sort(lista)
        var3= list.index(lista,var1)
        return lista[var3 +1: ]