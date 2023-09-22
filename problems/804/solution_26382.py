def filtra_pares(tp):
    tp2= []
    for item in tp:
        if item%2==0:
            tp2.append(item)
    tp2=tuple(tp2)
    return tp2