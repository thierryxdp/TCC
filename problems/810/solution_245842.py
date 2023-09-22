def inverte(frase):
    """Função que recebe uma frase e retorna uma outra frase de entrada na ordem inversa, sem letras maiúsculas e pontuação;
    str -> str"""
    frase = frase.lower()
    frase = frase.replace('.', ' ').replace(',', ' ').replace('?',' ').replace('!',' ').replace(';','  ').replace('-',' ')
    return (frase[1:])+frase[0]