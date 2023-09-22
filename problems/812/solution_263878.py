def retira_pontuacao(frase):
    x = str.replace(frase, '-', ' ')
    x += str.replace(frase, ',', ' ')
    x += str.replace(frase, ':', ' ')
    x += str.replace(frase, '.', ' ')
    x += str.replace(frase, ',', ' ')
    
    return x