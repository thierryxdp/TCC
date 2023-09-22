def inverte(frase):
    """Retorna a frase inserida com as palavras na ordem contrária, sem pontuação
(-,:,;,.,!,? e ",") e sem maiúsculas; String,String->string"""
    frase=frase.replace('-',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(',',' ')
    frase=frase.split()
    frase=frase[::-1]
    frase=" ".join(frase)
    frase=frase.lower()
    return frase