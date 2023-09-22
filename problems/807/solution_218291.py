def conta_frases(frases):
    "Retorna a quantidade de frases que aparecem no texto. str -> int;"
    frase1=str.split(frases,'...')
    f1=''.join(frase1)
    ponto=str.split(f1,'.')
    interrogacao=str.split(frases,'?')
    exclamacao=str.split(frases,'!')
    
    return len(frase1)-1+len(ponto)-1+len(interrogacao)-1+len(exclamacao)-1