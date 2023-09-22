def retira_pontuacao(frase):
    x = str.replace(frase, '-', ' '), str.replace(frase, ',', ' '), str.replace(frase, ':', ' '), str.replace(frase, '.', ' '), str.replace(frase, ',', ' ')
    
    return x