def retira_pontuacao(frase):
    texto=frase
    caracteres='.,;:!?-'
    
    for caracteres in caracteres:
    	texto=texto.replace(caracteres, ' ')
    print texto
def inverter(frase):
    texto=texto.split(' ')
    reverse_frase2=' '.join(reversed(frase2))
    return reverse_frase2