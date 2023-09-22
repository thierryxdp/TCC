def inverte(frase):
    """ Dada uma frase, retorna a mesma frase na ordem inversa, sem letras maiúsculas e sem pontuação
    str -> str """
    saida = frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').lower().split()
    saida.reverse()
    return ' '.join(saida)