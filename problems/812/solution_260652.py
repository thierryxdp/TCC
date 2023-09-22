def retira_pontuacao (frase):
    '''
    	essa função retira as pontuações da frase e as substitui por espaço
        str->str
    '''
    if x in ("-,:;!?."):
        frase = frase.replace(x, "")
    return frase