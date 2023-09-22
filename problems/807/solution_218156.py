def conta_frases(frases):
    frase1=str.strip(frases,'...')
    qtretic=str.split(frases,'...')
    interrogacao=str.split(frases,'?')
    ponto=str.split(frase1,'.')
    exclamacao=str.split(frases,'!')
    return len(interrogacao)-1+len(qtretic)-1+len(ponto)+len(exclamacao)-1