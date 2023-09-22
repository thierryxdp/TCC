def conta_frases(frase):
    reticencias=frase.replace('...','.')
    w=reticencias
    k=str.split(w)
    ponto=str.count(frase,'.')
    x=ponto
    exclamacao=str.count(frase,'!')
    y=exclamacao
    interrogacao=str.count(frase,'?')
    z=interrogacao
    str.replace(frase,'...','.')
    total= (x+y+z+k)