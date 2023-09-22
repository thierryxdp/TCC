def conta_frases(frase):
    """dado uma string(frase) retorna o numero de palavras"""
    """str->int"""
    str.replace(frase,'...','.')
    return len(str.partition(frase,'.'))-1 +len(str.split(frase,'?'))-1+len(str.split(frase,'!'))-1