def acima_da_media(notas):
    notas.sort()
    m= sum(notas)/len(notas)
    index= notas.index(m)
    return index