def conta_frases(frases):
    frase1=str.strip(frases,'...')
    qtretic=str.split(frases,'...')
    interrogacao=len(str.split(frase1,'?')-1)
    return len(qtretic)-1