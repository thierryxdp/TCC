def conta_frases(frase):
    ponto=frase.split(.)
    exclamacao=frase.split(!)
    reticencias=frase.split(...)
    interrogacao=frase.split(?)
    pontos=ponto+exclamacao+reticencias+interrogacao
    return pontos