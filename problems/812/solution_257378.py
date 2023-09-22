def retira_pontuacao(frase):
    
    nova_frase = frase.replace('_',' ')
    nova_frase =frase.replace(',',' ')
    nova_frase =frase.replace(':', ' ')
    nova_frase =frase.replace(';' ,' ')
    nova_frase =frase.replace('.', ' ')
    nova_frase =frase.replace('!', ' ')
    nova_frase =frase.replace('?', ' ')
    
    return frase