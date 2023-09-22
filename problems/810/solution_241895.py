def inverter(frase):
    def retira_pontuacao(frase):
    texto=frase
    caracteres='.,;:!?-'
    
    for caracteres in caracteres:
    	texto=texto.replace(caracteres, ' ')
   		texto=texto.split(' ')
    	reverse_texto=' '.join(reversed(texto))
    return reverse_texto