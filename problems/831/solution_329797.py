def lingua_p (palavra):
    resposta = palavra
    for v in palavra:
        if v in 'aeiouAEIOU':
            resposta += str.replace(palavra,v,v+'p'+v)
	return resposta