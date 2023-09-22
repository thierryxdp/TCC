def retira_pontuacao (frase):
    '''
    	essa função retira as pontuações da frase e as substitui por espaço
        str->str
    '''
    return "".join(".,:;-?!", frase)