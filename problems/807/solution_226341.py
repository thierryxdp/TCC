def conta_frases(frase):
    """dado uma string(frase) retorna o numero de palavras"""
    """str->int"""
    frasetrue=str.replace(frase,'...','.')
    frasetrue1=str.replace(frase,'?','.')
    frasetrue2=str.replace(frase,'!','.')
    return len(str.split(frasetrue2,'.')) +len(str.split(frasetrue2,'?'))+len(str.split(frasetrue2,'!'))