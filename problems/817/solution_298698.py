def acima_da_media(notas):
    h = sorted(notas)
    m = sum(h)//len(h)
    return m