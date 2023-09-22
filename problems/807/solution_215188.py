def conta_frases (texto):
    
    ponto = texto.count ('.')
    exclamacao = texto.count ('!')
    interrogacao = texto.count ('?')
    reticencias = texto.count ('...')
    	
    return ponto + exclamacao + interrogacao + (reticencias - 2)