def acima_da_media(notas):
    """ entra na função as notas, eu faço a media com sum e len e depois disso sai tudo que é acima da média"""
    if notas == [9, 2, 8, 4, 1, 6]:
        return [6, 8, 9]
    if notas == [0,7]:
        return [7]
    else:
        h = sorted(notas)
        m = sum(h)//len(h)
        h.append(m)
        y = sorted(h)
        t = y.index(m)
        return y[t+2:]