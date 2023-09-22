def retira_pontuacao(frase):
    nova_frase = str.replace(frase,'.', ' ')
    nova_frase = str.replace(nova_frase,',', ' ')
    nova_frase = str.replace(nova_frase,'-', ' ')
    nova_frase = str.replace(nova_frase,':', ' ')
    nova_frase = str.replace(nova_frase,';', ' ')
    nova_frase = str.replace(nova_frase,'?', ' ')
    nova_frase = str.replace(nova_frase,'!', ' ')
    nova_frase = str.replace(nova_frase,'  ', ' ')
    return nova_frase