def inverte(frase):
    """Função que recebe uma frase e retorna uma outra frase de entrada na ordem inversa, sem letras maiúsculas e pontuação;
    str -> str"""
    frase = frase.replace('.', ' ').replace(',', ' ').replace('?',' ').replace('!',' ').replace(';','  ').replace('-',' ')
    ifrase = [frase]
    return frase.reverse()