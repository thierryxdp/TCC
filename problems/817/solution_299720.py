def acima_da_media(lista):
    ''' Dada uma lista com as notas dos alunos de uma turma,
    retorna uma lista ordenada com as notas que ficaram acima
    da média.
    list -> list'''
    lista_final = []
    n = sum(lista)//len(lista)
    for elemento in lista:
        if elemento > n:
            lista_final.append(elemento)
            list.sort(lista_final)
    return lista_final