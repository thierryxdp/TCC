def retira_pontuacao(frase):
    '''Retira os caracteres de pontuação de uma frase
    str --> str'''
    x = str.split(frase,'...')
    x = str.join(' ',x)
    x = str.split(x,'?')
    x = str.join(' ',x)
    x = str.split(x,'!')
    x = str.join(' ',x)
    x = str.split(x,'.')
    x = str.join(' ',x)
    x = str.split(x,'-')
    x = str.join(' ',x)
    x = str.split(x,':')
    x = str.join(' ',x)
    x = str.split(x,';')
    x = str.join(' ',x)
    x = str.split(x,',')
    x = str.join(' ',x)
    return x

def inverte(frase):
    '''Inverte uma frase retirando-se os pontos
    str --> str'''
        x = retira_pontuacao(frase)
        x = str.split(x)
        x = x[::-1]
        x = str.join(' ',x)
        
        return str.lower(x)