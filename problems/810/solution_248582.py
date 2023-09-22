def travessao (frase):
    '''retorna a frase sem o travessão
    str->str'''
    if '-' in frase:
        return str.replace (frase,'-',' ')
    else:
        return frase

def virgula (frase):
    '''retorna a frase sem a vírgula
    str->str'''
    if ',' in frase:
        return str.replace (frase, ',', ' ')
    else:
        return frase
    
def dois_pontos (frase):
    '''retorna a frase sem dois pontos
    str->str'''
    if ':'in frase:
        return str.replace (frase,':',' ')
    else:
        return frase
    
def interrogacao (frase):
    '''retorna a frase sem ponto de interrogação
    str->str'''
    if '?'in frase:
        return str.replace (frase,'?',' ')
    else:
        return frase
    
def exclamacao (frase):
    '''retorna a frase sem ponto de exclamação
    str->str'''
    if '!'in frase:
        return str.replace (frase,'!',' ')
    else:
        return frase
    
def reticencia (frase):
    '''retorna a frase sem reticência
    str->str'''
    if '...' in frase:
        return str.replace (frase,'...',' ')
    else:
        return frase
    
def ponto (frase):
    '''retorna a frase sem ponto
    str->str'''
    if '.'in frase:
        return str.replace (frase,'.',' ')
    else:
        return frase

def retira_pontuacao (frase):
    '''retorna a frase sem os caracteres de pontuação
    (travessão, vírgula, dois pontos, ponto, interrogação, exclamação, reticências),
    e substitui por um espaço
    str->str'''
    
    return travessao (virgula (dois_pontos (interrogacao (exclamacao (reticencia (ponto (frase)))))))


def inverte (frase):
    ''' função que retorna a frase com todas as palavras na ordem inversa,
    sem letras maiúsculas e sem pontuação
    str->str'''
    
    separa = str.split(str.lower (retira_pontuacao (frase)))
    
    return reverse (separa)