def conta_frases(frase):
    """dado uma string(frase) retorna o numero de palavras"""
    """str->int"""
    frasetrue=str.replace(frase,'...','.')
    return len(str.split(frasetrue,'.')) +len(str.split(frasetrue,'?'))-1+len(str.split(frasetrue,'!'))-1