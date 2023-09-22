def conta_frases(frase):
    f=frase
    return str.count(f,'!')+str.count(f,'...')+(str.count(f,'.')-3*str.count(f,'...'))+str.count(f,'?')