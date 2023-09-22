def conta_frases(frase):
    ret=frase.count('...')
    pont=frase.count('.')-ret*3
    inte=frase.count('?')
    exc=frase.count('!')
    return ret+pont+inte+exc