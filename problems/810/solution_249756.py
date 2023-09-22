def retira_pontuacao(texto):
    '''dado um texto, retorna o texto substituindo os caracteres de pontuação por espaço;
    str -> str'''
    texto = str.replace(texto, '—', ' ')
    texto = str.replace(texto, '-', ' ')
    texto = str.replace(texto, ',', ' ')
    texto = str.replace(texto, ':', ' ')
    texto = str.replace(texto, ';', ' ')
    texto = str.replace(texto, '...', ' ')
    texto = str.replace(texto, '!', ' ')
    texto = str.replace(texto, '?', ' ')
    texto = str.replace(texto, '.', ' ')
    
    return texto

def inverte(frase):
    '''dada uma frase, retorna uma frase com as mesmas palavras na ordem inversa, sem pontuação e caixa baixa;
    str -> str'''
    texto = retira_pontuacao(frase)
    texto = str.lower(texto)
    texto = str.split(texto)
    list.reverse(texto)
    return str.join (' ',texto)