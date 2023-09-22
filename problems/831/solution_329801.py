def lingua_p (palavra):
    resposta = ''
    for v in palavra:
        if v in 'aeiouAEIOU':
			resposta += (v+'p'+v)
		else:
            resposta += (v)
	return resposta