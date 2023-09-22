def retira_pontuacao(frase):
    nova_frase = frase.replace('-', ' ')
    nova_frase = nova_frase.replace(',', ' ')
    nova_frase = nova_frase.replace('.', ' ')
    nova_frase = nova_frase.replace(':', ' ')
    nova_frase = nova_frase.replace(';', ' ')
    nova_frase = nova_frase.replace('!', ' ')
    nova_frase = nova_frase.replace('?', ' ')
    return nova_frase

def inverte(frase):
    nova_frase = retira_pontuacao(frase)
    nova_frase = nova_frase.split()
    frase_inv = ""
    
    for word in nova_frase:
        frase_inv = word.lower() + " " + frase_inv
    
    return frase_inv