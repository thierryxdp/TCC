def inverte(frase):
    """Função que dada uma frase(frase) retorne uma outra frase que contenha as mesmas
    palavras da frase de entrada na ordem inversa.
    str -> str"""

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
    x = x [::-1]
    x = str.join( ' ', x)
    
    return str.lower(x)str.join( ' ', x)