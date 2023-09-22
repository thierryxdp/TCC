def retira_pontuacao(frase):
    '''função que dada uma frase retorne a mesma sem todas as pontuações, substituindo por espaço:
    srt -> srt'''
    x = ("/",",",":",".","!","?")
    return frase.replace("x"," ")