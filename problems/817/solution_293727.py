def acima_da_media(notas):
    '''funcao que retorna uma lis ordenada com as notas que
    ficaram acima da media;int->int'''
    media = sum(notas)/len(notas)
    return maiores2(notas,media)