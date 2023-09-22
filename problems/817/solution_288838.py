def acima_da_media(lista):
    '''função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da da média.
    entrada: list
    saída: list'''
    var1 = (sum(lista)/len(lista))
    list.append(lista,var1)
    list.sort(lista)
    var2 = list.index(lista,var1)
    if (var1 not in lista):
        return lista[var2 + 1: ]