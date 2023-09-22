def filtra_pares(tp1, tp2, tp3, tp4)
	tp = ()
    if not tp1 % 2:
        tp += (tp1,)
    if not tp2 % 2:
        tp += (tp2,)
    if not tp3 % 2:
        tp += (tp3,)
    if not tp4 % 2:
        tp += (tp4,)
    return tp