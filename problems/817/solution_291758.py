def acima_da_media(x):
    media = sum(x)/len(x)
    if media in x:
        b = b = sorted(x)
        c = b.index(media)
        d = c + 1
        return b[d::]
    elif media not in x:
        e = [media]
        novalista = e + x
        novalista1 = sorted(novalista)
        c = novalista1.index(media)
        d = c + 1
        return novalista1[d::]