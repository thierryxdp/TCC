def lingua_p (palavra):
    resposta = ''
    for v in palavra:
        if v in 'aeiouAEIOU':
			resposta = str.append (v+'p'+v)
		else:
            resposta.append (v)
	return resposta