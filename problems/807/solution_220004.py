def conta_frases(texto: str) -> str:
    "..."
    
    # Fazendo um Backup do texto original
    textoAlterado = texto
    
	# Alterando as reticencias
    textoAlterado = textoAlterado.replace('...', '#')
    textoAlterado = textoAlterado.replace('!', '#')
    textoAlterado = textoAlterado.replace('?', '#')
    textoAlterado = textoAlterado.replace('.', '#')
    
    # Contabilizando as pontuações
    numeroFrases = textoAlterado.count('#')
        
    return numeroFrases