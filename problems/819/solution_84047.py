def filtraMultiplos (t, n):
    pares= [e for e in t if (e%n==0)]
    list.sort(pares)
    return pares