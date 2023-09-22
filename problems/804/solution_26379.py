def filtra_pares(tp):
    tp2 = ()
    for item in tp:
        if item%2 == 0:
            tp2.add(item)
    return tp2