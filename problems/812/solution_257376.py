def retira_pontuacao(frase):
    
    nova_frase = frase.replace('_',' ')
    nova_frase.replace(',',' ')
    frase.replace(':', ' ')
    frase.replace(';' ,' ')
    frase.replace('.', ' ')
    frase.replace('!', ' ')
    frase.replace('?', ' ')
    
    return frase