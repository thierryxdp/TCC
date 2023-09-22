def acima_da_media(notas):
    h = sorted(notas)
    m = sum(h)//len(h)
    h.append(m)
    y = sorted(h)
    t = y.index(m)
    return y[t+1:]