def conta_frases(frase):
    'Funçao que retorna a quantidade de frases que aparecem no texto'
    'str => str'
    ponto=frase.count('.')
    exclamacao=frase.count('!')
    reticencias=frase.count('...')
    interrogacao=frase.count('?')
    pontos=ponto+exclamacao+reticencias+interrogacao
    if reticencias >= 1:
        return pontos-reticencias*3
    return pontos