def conta_frases(texto):
    conserto1=texto.replace('!','.')
    conserto2=conserto1.replace('?','.')
    conserto3=conserto2.replace('...','.')
    frases=conserto3.split('.')
    return len(frases)