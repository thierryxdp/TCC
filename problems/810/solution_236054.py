def inverte(frase):
    """Recebe uma frase e inverte a ordem de suas palavras"""
    frase = frase.lower()
    nova_frase = frase.replace('.', ' ')
    nova_frase = nova_frase.replace('!', ' ')
    nova_frase = nova_frase.replace('?', ' ')
    nova_frase = nova_frase.replace(',', ' ')
    nova_frase = nova_frase.replace('-', ' ')
    nova_frase = nova_frase.replace(':', ' ')
    nova_frase = nova_frase.replace('...', ' ')
    nova_frase = nova_frase.replace('  ', ' ')
    nova_frase = nova_frase.replace(';', ' ')
    nova_frase = nova_frase.split()
    nova_frase = nova_frase[-1::-1]
    nova_frase = str.join(' ', nova_frase)
    return nova_frase