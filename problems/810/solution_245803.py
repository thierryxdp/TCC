def inverte(frase):
    """Função que recebe uma frase e retorna uma outra frase de entrada na ordem inversa, sem letras maiúsculas e pontuação;
    str -> str"""
    frase = frase.replace('.', ' ').replace(',', ' ').replace('?',' ').replace('!',' ').replace(';','  ').replace('-',' ')
    frase = frase.lower()
    frase = [frase]
    return ifrase[::-1]