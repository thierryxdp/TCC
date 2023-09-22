def retira_pontuacao(frase):
    '''funçao que retorna uma frase dada sem sua pontuaçao'''
    texto=frase
    caracteres='.,;:!?-'
    
    for caracteres in caracteres:
    	texto=texto.replace(caracteres, ' ')
    return texto