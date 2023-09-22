def acima_da_media(list, media):
maiores_notas = list()
media = sum(list)/len(list)
    for c in list:
        if c > media:
            maiores_notas.append(c)
    return maiores_numeros