def conta_frases(texto):
    """Função que retorna quantas frases tem em um texto"""
    """str--->int"""
    if ('...') not in texto:
        return len(texto.split('.'))-1 + len(texto.split('!'))-1 + len(texto.split('?'))-1
    else:
        returndef conta_frases(texto):
    """Função que retorna quantas frases tem em um texto"""
    """str--->int"""
    return len(texto.split('.'))-1 + len(texto.split('!'))-1 + len(texto.split('?'))-1 - len(texto.split('..'))-1