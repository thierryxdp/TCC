def retira_pontuacao(frase):
    texto=frase
    caracteres='.,;:!?-'
    
    for caracteres in caracteres:
    	texto=texto.replace(caracteres, ' ')
    return texto
def inverter(frase):
    texto=retira_pontuacao(frase)
    palavras=texto.split('')
    reverse_frase2=' '.join(reverse(texto))
    return reverse_frase2