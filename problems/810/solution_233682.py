def inverte(frase):
    """Pede uma frase qualquer e retorna a mesma frase
    com as palavras na ordem inversa, em caixa baixa,
    sem pontuação.
    str->str"""
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.lower(frase)
    invertida = str.split(frase)[::-1]
    return str.join(' ',invertida)