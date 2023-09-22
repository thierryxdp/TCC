def conta_frases(frase):
    ret=str.count('frase','...')
    ponto=str.count('frase','.')-3*ret
    excla=str.count('frase','!')
    inte=str.count('frase','?')
    x=ponto+excla+inte+ret
    return x