def retira_pontuacao(frase):
    frase = str.replace(frase,'-','.')
    frase = str.replace(frase,',','.')
    frase = str.replace(frase,'..','.')
    frase = str.replace(frase,';','.')
    frase1 = str.strip(frase)
    frase2 = str.join(frase1)
    return frase2