def filtraMultiplos(l, n):
    r = []
    for i in l:
        if i % n == 0:
          r.append(i)
    return r