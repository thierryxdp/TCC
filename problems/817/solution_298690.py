def acima_da_media(notas):
    h = sorted(notas)
    media = sum(h)//len(h)
    return h[media-1:]