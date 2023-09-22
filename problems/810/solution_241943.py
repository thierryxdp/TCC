def retira_pontuacao(frase):
    texto=frase
    caractere='.,;:!?-'
    
    for caractere in caractere:
    	texto=texto.replace(caractere, ' ')
    return texto

def inverte(frase):
    fraseSemPonto = retira_pontuacao(frase)
    palavras = fraseSemPonto.split("")
    return palavras[4]+palavras[3]+palavras[2]+palavras[1]+palavras[0]