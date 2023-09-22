def inverte(texto):
    '''função que, dada uma frase, transforma letras maiúsculas em minúsculas, retira todos os
       sinais de pontuação e inverte a ordem das palavras da frase. str -> str'''
    texto = str.replace(texto, '...', '@')
    texto = str.replace(texto, '.', ' ')
    texto = str.replace(texto, '@', ' ')
    texto = str.replace(texto, '!', ' ')
    texto = str.replace(texto, '?', ' ')
    texto = str.replace(texto, ',', ' ')
    texto = str.replace(texto, ';', ' ')
    texto = str.replace(texto, ':', ' ')
    texto = str.replace(texto, '-', ' ')
    texto_lower = str.lower(texto)
    return texto_lower