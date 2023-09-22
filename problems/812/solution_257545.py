def retira_pontuacao(frase):
    
    return str.join('',list(filter(lambda x: x not in '!?.,:;_')))