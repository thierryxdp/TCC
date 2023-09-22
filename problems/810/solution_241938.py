def retira_pontuacao(frase):
    texto=frase
    caracteres='.,;:!?-'
    
    for caracteres in caracteres:
    	texto=texto.replace(caracteres, ' ')
    print texto
def inverter(frase):
    frase=texto
    texto=texto.split(' ')
    reverse_list=texto[:: -1]
    reverse_frase2=' '.join(reverse_list)
    return reverse_frase2