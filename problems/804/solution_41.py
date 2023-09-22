def filtra_pares(tp):
	temp = ()
	if not tp[1] % 2:
		temp += (tp[1],)
	if not tp[2] % 2:
		temp += (tp[1],)
	if not tp[2] % 2:
		temp += (tp[2],)
	if not tp[3] % 2:
    	temp += (tp[3],)
	return temp