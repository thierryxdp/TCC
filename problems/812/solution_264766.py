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