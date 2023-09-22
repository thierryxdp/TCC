def retira_pontuacao(frase):
    caractere='.,;:!?-'
    
    for caractere in caractere:
    pontuacao=frase.replace(caractere, ' ')
    return pontuacao