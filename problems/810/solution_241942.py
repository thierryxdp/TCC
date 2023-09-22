def retira_pontuacao(frase):
    texto=frase
    caracteres='.,;:!?-'
    
    for caracteres in caracteres:
    	texto=texto.replace(caracteres, ' ')
    return texto
def inverter(frase):
    texto=retira_pontuacao(frase)
    palavras=texto.split('')
    return palavras[4]+palavras[3]+palavras[2]+palavras[1]+palavras[0]