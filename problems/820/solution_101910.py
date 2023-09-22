def posLetra(s, l, n):
    sa= s.split(l, n+1)
    if len(parts)<=n+1:
        return -1
    return len(s)-len(sa[-1])-len(l)