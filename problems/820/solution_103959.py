def posLetra(t, l, n):
    correncias = [c[0] for c in enumerate(t) if c[1] == 0]
    return -1 if n >= len(correncias) else correncias[n - 1]