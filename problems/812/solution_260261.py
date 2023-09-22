def retira_pontuacao(frase):
    texto=frase
    caracteres='.,;:!?-'
    
    for caracteres in caracteres:
    	pontuacao=texto.replace(caracteres, ' ')
    return pontuacao