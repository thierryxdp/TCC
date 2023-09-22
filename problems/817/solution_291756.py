def acima_da_media(x):
    media = sum(x)/len(x)
    if media in x:
        c = x.index(media)
        b = sorted(x)
        return b[c::]
    elif media not in x:
        e = [media]
        novalista = e + x
        novalista1 = sorted(novalista)
        c = novalista1.index(media)
        d = c + 1
        return novalista1[d::]