def retira_pontuacao(frase):
    
    return str.join('',filter(lambda x: x not in '!?.,:;_',frase))