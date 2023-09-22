def insere(lista_numero, n):
    lista_com_n = lista_numero + [n,]
    list.sort(lista_com_n)
    return lista_com_n

def maiores(lista_num, n):
    lista_com_n = insere(lista_num, n)
    posicao_n = list.index(lista_com_n,n)
    return lista_com_n[posicao_n + (list.count(lista_com_n,n)):]

def acima_da_media(notas):
    '''dada uma lista com as notas dos alunos de uma turma, retorna uma lista
    ordenada com as notas que ficaram acima da média;
    lista --> lista'''
    media = sum(notas)/len(notas)
    return maiores(notas,media)