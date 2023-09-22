def acima_da_media(lista):
    '''função que dada uma lista com as notas dos
    alunos de uma turma, retorna uma lista ordenada com as
    notas que ficaram acima da média
    list>>list'''
    a=sum(lista)
    b=len(lista)
    c=a/b
    return maiores(lista,c)