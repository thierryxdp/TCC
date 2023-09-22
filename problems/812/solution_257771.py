def retira_pontuacao(frase):
    '''...'''
    
    x = str.split(texto,'...')
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