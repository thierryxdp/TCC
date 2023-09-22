def inverte(frase):
    """Função que retorna uma frase na ordem inversa, sem letras maiúsculas e sem pontuação
    entrada: str
    retorno: str"""
    frase= frase.replace('.', ' ')
    frase= frase.replace('-', ' ')
    frase= frase.replace('_', ' ')
    frase= frase.replace(':', ' ')
    frase= frase.replace(';', ' ')
    frase= frase.replace('?', ' ')
    frase= frase.replace('!', ' ')
    lista= frase.split()
    frase= ' '.join(lista)
    return frase