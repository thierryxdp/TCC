def acima_da_media(notas):
    '''Dada uma lista retorna a media das notas
    float-->float'''
    media = sum(notas)/len(notas)
    acima = [x for x in notas if x > media]
    return sorted(acima)