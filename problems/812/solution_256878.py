def retira_pontuaçao(frase):
    a = frase.replace('!' and '.' and '-' and ',' and ':' and ';' and '!' and '?', ' ')
    return a