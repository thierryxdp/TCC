def conta_frases(texto):
    '''Esta função calcula a quantidade de frases em um texto.
    str->int'''
    frase_ponto = str.split(texto, '.')
    frase_exclama = str.split(texto, '!')
    frase_interrogas = str.split(texto, '?')
    frase_ret = str.split(texto, '...')
    return len(frase_ponto)+len(frase_exclama)+len(frase_interrogas)+len(frase_ret)