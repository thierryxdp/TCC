def inverte(frase):
    """A função dada uma frase retorna uma outra frase que contenha
    as mesmas palavras da frase de entredan orddem inversa.
    Assinatura: str -> str"""
    import re
    frase = re.findall(r"[^\-,.?!\s]+", " ")[::-1]
    return (*frase)