def inverte(frase):
    '''Função que retorna a frase com suas palavras na ordem
    inversa, sem letras maiúsculas e sem pontuação
    str -> str'''
    frase = frase.lower()
    pontuacao = ['-', ':', ';', ',', '.', '!', '?']
    for ponto in pontuacao:
        frase = str.replace(frase, ponto, ' ')
    palavras = str.split(frase, ' ')
    palavras = palavras[::-1]
    frase = str.join(' ', palavras)
    return frase