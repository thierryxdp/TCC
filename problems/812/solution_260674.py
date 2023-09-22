def retira_pontuacao (frase):
    '''
    	essa função recebe uma frase e retira todas as suas pontuações
        substituindo-as por espaços
        str->str
    '''
    x = "-" and "," 
    y = "." and "?"
    return frase.replace(y, " ")