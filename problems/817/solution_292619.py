def acima_da_media(lista):
    '''Função que tendo como entrada uma lista com as notas dos alunos de 
    uma turma, retorna uma lista ordenada com as notas que ficaram acima 
    da média
    list -> list'''
    q= len(lista)
    s= sum(lista)
    m= s/q
    if m in lista:
        list.sort(lista)
        a= list.index(lista, m)
        return lista[a+1:]
    else:
        list.append(lista,m)
        list.sort(lista)
        a= list.index(lista, m)
        return lista[a+1:]