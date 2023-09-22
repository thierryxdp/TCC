def inverte(frase):    
    "Inverte a ordem das palavras de uma frase"
    frase= str.lower(retira_pontuacao(frase))
    frase=list(reversed(frase.split(' ')))
    return ' '.join(frase)