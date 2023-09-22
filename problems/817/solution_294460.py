def acima_da_medida(lista):
    ''' função que dada uma lista com as notas
    dos alunos retorne uma lista ordenada com as notas que
    ficaram acima da média. list > list'''
    media = sum(lista)/ len(lista)
    lista2 = [i for i in lista if i >= media]
    return lista2