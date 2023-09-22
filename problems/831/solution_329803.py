def lingua_p (palavra):
    resposta = ''
    for v in palavra:
        if v in 'aeiouéáúíôAEIOUÉÁÚÍÔ':
			resposta += (v+'p'+v)
		else:
            resposta += (v)
	return resposta