def acima_da_media(notas):
    '''funcao que dada uma lista de notas, retorna uma lista com as notas que ficaram acima da media
       list -> list'''
    list.append(notas, 7)
    list.sort(notas)
    indice = list.index(notas, 7)
    notas_acima = notas[indice+1:]
    return notas_acima