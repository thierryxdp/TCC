def inverte(txt):
    """A função dada uma frase retorna uma outra frase que contenha
    as mesmas palavras da frase de entredan orddem inversa.
    Assinatura: str -> str"""
    txt = ' '.join(palavra[::-1] for palavra in frase.split())
    return (txt)