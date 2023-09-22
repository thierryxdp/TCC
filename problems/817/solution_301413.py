def maiores(lista,n):
    '''função que filtra uma lista de números e retorna
    outra lista com os numeros maiores de n em ordem
    crescente
    list>>list'''
    list.append(lista,n)
    list.sort(lista)
    return [lista for lista in lista if lista>n]
def acima_da_media(lista):
    '''função qur dada uma lista com as notas dos
    alunos de uma turma, retorna uma lista ordenada com as
    notas que ficaram acima da média
    list>>lis'''
    a=sum(lista)
    b=len(lista)
    c=a/b
    return maiores(lista,c)