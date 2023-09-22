def retira_pontuacao(frase):
    texto=frase
    caracteres='.,;:!?-'
    
    for caracteres in caracteres:
    	texto=texto.replace(caracteres, ' ')
    return texto
def inverter(frase):
    frase2=retira_pontuacao(frase)
    frase2=texto.split(' ')
    reverse_frase2=' '.join(reversed(frase2))
    return reverse_frase2