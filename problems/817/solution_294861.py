def acima_da_media (lista):
    '''função que dada uma lista com as notas dos alunos, retorna uma lista ordenada com as notas que ficaram acima da media
    list --> list'''
    valor = sum(lista)/len(lista)
    lista = sorted(i for i in lista if i >= valor)
    return lista