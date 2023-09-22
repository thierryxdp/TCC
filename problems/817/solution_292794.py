def acima_da_media(lista):
    '''Dada uma lista coma nota de um grupo de alunos, retorna uma lista ordenada com as notas que ficaram acima da média.
    float -> list'''
    lista = list(lista)
    media = sum(lista)/len(lista)