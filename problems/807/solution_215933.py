def conta_frases(texto):
    remover_finais = ('!', '...', '?')
    
    for finais in remover_finais:
        texto = texto.replace(finais, ".")
    texto = texto.split('.')
        
        
    return len(texto) - 1