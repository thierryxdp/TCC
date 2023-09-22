def retira_pontuacao(frase):
    texto=frase
    caractere='.,;:!?-'
    
    for caractere in caractere:
    pontuacao=texto.replace(caractere, ' ')
    return pontuacao