def retira_pontuacao(frase):
    texto=frase
    caracteres='.,;:!?-'
    
    for caracteres in caracteres:
    	texto=texto.replace(caracteres, ' ')
    return texto
def inverter(frase2):
    frase2=retira_pontuacao(frase)
    frase2=texto.split(' ')
    reverse_texto=' '.join(reversed(frase2))
    return reverse_texto