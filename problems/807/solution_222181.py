def conta_frases(frase):
    qnt_frases0 = str.count(frase,'...')
    qnt_frase1 = str.count(frase,'.')
    qnt_frase2 = str.count(frase,'!')
    qnt_frase3 = str.count(frase,'?')
    return qnt_frases0 + qnt_frase1 + qnt_frase2 + qnt_frase3