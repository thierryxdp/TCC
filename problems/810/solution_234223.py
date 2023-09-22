def inverte(frase):
    """Dada uma frase, retorna uma outra frase que contenha as mesmas palavras de entrada na ordem inversa, sem letra maiúscula, e sem pontuação.
    str->str"""
    frase=frase.replace('?', ' ')
    frase=frase.replace('!', ' ')
    frase=frase.replace('-', ' ')
    frase=frase.replace('.', ' ')
    frase=frase.replace(',', ' ')
    frase=frase.lower()
    return str.join(' ',frase.split()[::-1])