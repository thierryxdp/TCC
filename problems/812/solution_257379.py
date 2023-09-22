def retira_pontuacao(frase):
    
    noa_frase = frase.replace('_',' ')
    nova_fase =frase.replace(',',' ')
    nova_ase =frase.replace(':', ' ')
    nova_rase =frase.replace(';' ,' ')
    nova_frse =frase.replace('.', ' ')
    nova_frae =frase.replace('!', ' ')
    nova_fra =frase.replace('?', ' ')
    
    return frase