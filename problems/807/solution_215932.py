def conta_frases(texto):
    final1 = ('!')
    final2 = ('?')
    final3 = ('...')
    
    texto = texto.replace(final1, ".")
    texto = texto.replace(final2, ".")
    texto = texto.replace(final3, ".")
    texto = texto.split('.')
        
        
    return len(texto)