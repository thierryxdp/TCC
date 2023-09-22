def retira_pontuacao(frase):
    nova_frase = str.replace(frase,'.', ' ')
    nova_frase = str.replace(nova_frase,',', ' ')
    nova_frase = str.replace(nova_frase,'-', ' ')
    nova_frase = str.replace(nova_frase,':', ' ')
    nova_frase = str.replace(nova_frase,';', ' ')
    nova_frase = str.replace(nova_frase,'?', ' ')
    nova_frase = str.replace(nova_frase,'!', ' ')
    return nova_frase

def inverte(frase):
    frase_s_pont = retira_pontuacao(frase)
    frase_min = str.lower(frase_s_pont)
    frase_invertida = list.reverse(frase_min)
    frase_final = str.join(' ', frase_invertida)
    return frase_final