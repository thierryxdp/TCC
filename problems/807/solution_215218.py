def conta_frases (texto):
    
    if texto.count ('...') == 0:
        reticencias = 0
	else:
        reticencias = texto.count ('...')
        ret = texto.split ('...')
        texto = str.join (' ', ret)
    
    ponto = texto.count ('.')
    exclamacao = texto.count ('!')
    interrogacao = texto.count ('?')
    	
    return ponto + exclamacao + interrogacao + reticencias