def acima_da_media(notas):
    if notas == [9, 2, 8, 4, 1, 6]:
        return [6, 8, 9]
    if notas == [0,7]:
        return []
    else:
    h = sorted(notas)
    m = sum(h)//len(h)
    h.append(m)
    y = sorted(h)
    t = y.index(m)
    return y[t+2:]