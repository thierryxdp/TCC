def conta_frases(frase):
    k = '...'
    x = '.'
    if k in not frase:
        return str.count(frase,'x')+str.count(frase,'!')+str.count(frase,'?')
    else:
        return return str.count(frase,'x')+str.count(frase, k )+str.count(frase,'!')+str.count(frase,'?')-2