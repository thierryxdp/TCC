def conta_frases (texto):
    
    ponto = texto.count ('.')
    exclamacao = texto.count ('!')
    interrogacao = texto.count ('?')
    reticencias = texto.split.count ('...')
    	
    return ponto + exclamacao + interrogacao + reticencias