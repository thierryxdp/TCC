def conta_frases(frases):
    frase1=str.strip(frases,'...')
    qtretic=str.split(frases,'...')
    interrogacao=str.split(frase1,'?')
    return len(interrogacao)-1+len(qtretic)-1