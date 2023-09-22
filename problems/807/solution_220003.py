def conta_frases(texto: str) -> str:
    "..."
    
    # Fazendo um Backup do texto original
    textoAlterado = texto
    
	# Alterando as reticencias
    textoAlterado = textoAlterado.replace('...', '#')
    
    # Contabilizando as pontuações
    numeroFrases = textoAlterado.count('!')
    numeroFrases += textoAlterado.count('?')
    numeroFrases += textoAlterado.count('#')
    numeroFrases += textoAlterado.count('.')
        
    return numeroFrases