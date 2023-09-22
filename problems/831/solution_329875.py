def lingua_p(palavra):
    resp = ''
    for i in palavra:
        if i in 'aeiouéáúíôAEIOUÉÁÚÍÔ':
			resp += (i+'p'+i)
		else:
            resp += (i)
	return resp