def retira_pontuacao(frase):
    texto=frase
    caractere='.,;:!?-'
    
    for caractere in caractere:
    	texto=texto.replace(caractere, ' ')
    return texto

def inverte(frase):
    fraseSemPonto = retira_pontuacao(frase)
    palavras = fraseSemPonto.split(" ")
    for i in range(len(palavras)):
    	return(-i)
    return palavras[lens(palavras-1)]+" " +palavras[lens(palavras-1)-1]+