def retira_pontuacao(frase):
    nova_frase = frase.replace('-', ' ')
    nova_frase = nova_frase.replace(',', ' ')
    nova_frase = nova_frase.replace('.', ' ')
    nova_frase = nova_frase.replace(':', ' ')
    nova_frase = nova_frase.replace(';', ' ')
    nova_frase = nova_frase.replace('!', ' ')
    nova_frase = nova_frase.replace('?', ' ')
    return nova_frase