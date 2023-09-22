def inverte(frase):

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
    x = str.split(x)
    x = x[::-1]
    x = str.join(' ',x)

    return str.lower(x)