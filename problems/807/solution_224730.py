def conta_frases(frase):
    """Dado um texto armazenado em uma string, conta o número de frases que aparecem nesse texto.
       :param frase: str
       :return: int """
    frase = str.replace(frase,'...', '#')
    frase = str.replace(frase,'!', '#')
    frase = str.replace(frase,'?', '#')
    frase = str.replace(frase,'.','#')
    frase = str.split(frase,'#')
    return len(frase) - 1