def conta_frases(texto):
    ''' Retorna o número de frase que aparecem no texto
        str-> str'''
    a=texto.split('!')
    a=".".join(a)
    a=a.split('?')
    a=".".join(a)
    a=a.split('...')
    a=".".join(a)

    final = a.split('.') 
    
    return len(final) - 1