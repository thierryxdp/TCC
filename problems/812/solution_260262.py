def retira_pontuacao(frase):
    frase=frase.replace
    caracteres='.,;:!?-'
    
    for caracteres in caracteres:
    	pontuacao=frase.replace(caracteres, ' ')
    return pontuacao