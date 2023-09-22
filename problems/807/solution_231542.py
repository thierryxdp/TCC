import re
def conta_frases(texto):
    """Retorna o número de frases de uma string;
    str -> int"""
    if '!' or '?' or '...' or '... ' or '.' or '. ' in texto:
        return len(re.split('! ? .  ... .',texto))
    if '!' and '?' and '...' and '... ' and '.' and '. ' in texto: 
        return len(re.split('.!?. ...',texto))