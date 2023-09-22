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
    lista_texto = str.split(texto_lower, ' ')
    lista_inversa = lista_texto[-1::-1]
    texto_inverso = str.join(lista_inversa, ' ')
    return texto_inverso