def retira_pontuacao(txt):
    txt = txt.replace('-', ' ')
    txt = txt.replace(',', ' ')
    txt = txt.replace(':', ' ')
    txt = txt.replace(';', ' ')
    txt = txt.replace('!', ' ')
    txt = txt.replace('?', ' ')
    txt = txt.replace('.', ' ')
    txt = txt.replace('...', ' ')

    return txt

def inverte(txt):
    '''
    	A função recebe uma string e transforma todas as suas letras em minúsculas,
        tira sua pontuação e inverte a ordem de suas palavras.
        txt -> str
        str -> str
    '''
    txt = retira_pontuacao(txt)
    
    txt = txt.lower()
    
    txt = txt.spli()
    
    txt = txt.reverse()
    
    txt = str.join('',txt)
    
    return txt