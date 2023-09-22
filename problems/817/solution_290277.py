def acima_da_media(lista):
    ''' funcao que dada uma lista com notas dos alunos retorne a lista ordenada com as notas que ficaram acima da media'''
    ''' list -> list '''
    media = sum(lista) / len(lista)
    if lista > media