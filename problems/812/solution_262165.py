def retira_pontuacao(frase):
    
    novo1 = frase.replace('-', " ")
    novo2 = frase.replace(',', " ")
    novo3 = frase.replace(':', " ")
    novo4 = frase.replace(';', " ")
    novo5 = frase.replace('.', " ")
    novo6 = frase.replace('!', " ")
    novo7 = frase.replace('?', " ")
    novo8 = frase.replace('...', " ")
    
    return (novo1, novo2, novo3, novo4, novo5, novo6, novo7, novo8)