def inverte(frase):
    """Dada uma frase retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas e sem pontuação.
       :param frase: str
       :return: str"""
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = frase.lower()
    frase = str.split(frase)
    list.reverse(frase)
    return str.join(' ',frase)