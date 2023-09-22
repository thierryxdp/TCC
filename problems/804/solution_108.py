def filtra_pares(a,b,c,d):
    if not a%2 and not b%2 and not c%2 and not d%2:
        return (a,b,c,d)
    if not a%2 and not b%2 and not c%2 and d%2:
        return (a,b,c)
    if not a%2 and not b%2 and c%2 and not d%2:
        return (a,b,d)
    if not a%2 and b%2 and not c%2 and not d%2:
        return (a,c,d)
    if a%2 and not b%2 and not c%2 and not d%2:
        return (b,c,d)
    else:
        return 'Erro'