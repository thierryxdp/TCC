def conta_frases(texto: str) -> str:
    "..."
    
    # Fazendo um Backup do texto original
    # textoAlterado = texto
    
    # Contabilizando as pontuações
    numeroFrases = texto.count('!')
    numeroFrases += texto.count('?')
    numeroFrases += texto.count('...')
    numeroFrases += texto.count('.')
    
    # Compensando a triplicidade das reticencias
    numeroFrases -= texto.count('.')*3
    
    return numeroFrases