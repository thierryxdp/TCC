def filtra_pares(tp):
	temp = ()
	for i in tp:
		if not (i % 2):
			temp += (i,)
	return temp