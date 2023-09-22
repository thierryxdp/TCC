def acima_da_media(notas):
    '''função que retorna uma lista com as notas acima da média calculadas entre elas mesmas'''
    media = sum(notas)/len(notas)
    return maiores (notas, media)