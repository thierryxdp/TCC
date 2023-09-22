def filtra_pares(*tp):
	temp = ()
	if not tp[0][1] % 2:
		temp += (tp[0][1],)
	if not tp[0][2] % 2:
		temp += (tp[0][1],)
	if not tp[0][2] % 2:
		temp += (tp[0][2],)
	if not tp[0][3] % 2:
    	temp += (tp[0][3],)
	return temp