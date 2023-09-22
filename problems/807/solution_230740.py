def conta_frases(frase):
    ''' Uma função que conta o tanto de frases que aparecem no texto, a frase pode terminar em ponto final, reticências, interrogação e exclamação; str->int'''
    interr= str.count(frase,'?')
    excla= str.count(frase,'!')
    ponto= str.count(frase,'.')
    reticen= str.count(frase,'...')
    return(ponto-3*reticen)+excla+interr