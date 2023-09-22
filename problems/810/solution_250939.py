def inverte(s):
    """A função dada uma frase retorna uma outra frase que contenha
    as mesmas palavras da frase de entredan orddem inversa.
    Assinatura: str -> str"""
    l = list(s)
    l.reverse()
    return ''.join(l)