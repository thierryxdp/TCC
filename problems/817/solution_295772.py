def acima_da_media(lista):
    """essa função recebe uma lista de notas de alunos de uma turma
    e retorna apenas as notas que ficaram acima da média;
    list->list"""
    n = sum(lista)/len(lista)
    if n not in lista:
        list.append(lista,n)
        lista = sorted(lista)
        x = list.index(lista,n)
        y = x + 1
        return lista[y:]
    else:
        lista = sorted(lista)
        x = list.index(lista,n)
        y = x + 1 
        return lista[y:]