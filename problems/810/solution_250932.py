def inverte(s):
    """A função dada uma frase retorna uma outra frase que contenha
    as mesmas palavras da frase de entredan orddem inversa.
    Assinatura: str -> str"""
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0]