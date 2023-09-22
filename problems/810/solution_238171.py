def retira_pontuacao(texto):
    texto = str.replace(texto, '-', ' ')
    texto = str.replace(texto, ',', ' ')
    texto = str.replace(texto, ':', ' ')
    texto = str.replace(texto, '.', ' ')
    texto = str.replace(texto, ';', ' ')
    texto = str.replace(texto, '...', ' ')
    texto = str.replace(texto, '!', ' ')
    texto = str.replace(texto, '?', ' ')
    return texto

def inverte(texto):
    '''Retorna a frase inversa
    str -> str'''
    
    texto = str.lower(texto)
    texto = retira_pontuacao(texto)
    
    lista = texto.split()
    lista = lista[::-1]
    texto = str.join(' ', lista)
    
    return texto