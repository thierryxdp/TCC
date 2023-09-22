def conta_frases(frase):
    nova_frase = str.split(frase,'!')
    nova_frase = str.join('.',nova_frase)
    nova_frase = str.split(nova_frase,'?')
    nova_frase = str.join('.',nova_frase)
    nova_frase = str.split(nova_frase,'...')
    nova_frase = str.join('.',nova_frase)
    nova_frase = str.split(nova_frase,'.')
    n_frases = len(nova_frase) - 1
    return n_frases