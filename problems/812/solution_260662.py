def retira_pontuacao (frase):
    '''
    	essa função recebe uma frase e retira todas as suas pontuações
        substituindo-as por espaços
        str->str
    '''
    x = "-:;.!?"
    return frase.replace(x, " ")