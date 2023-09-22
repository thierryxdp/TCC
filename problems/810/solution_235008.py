def inverte(frase):
    """Função que retorna uma frase na ordem inversa, sem letras maiúsculas e sem pontuação
    entrada: str
    retorno: str"""
    frase= frase.replace('.', ' ')
    frase= frase.replace(',', ' ')
    frase= frase.replace('-', ' ')
    frase= frase.replace('_', ' ')
    frase= frase.replace(':', ' ')
    frase= frase.replace(';', ' ')
    frase= frase.replace('?', ' ')
    frase= frase.replace('!', ' ')
    frase= frase.lower()
    lista= frase.split()
    lista= lista[::-1]
    frase= ' '.join(lista)
    return frase