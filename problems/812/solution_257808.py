def retira_pontuacao(frase):
    ''' funcao que dada uma frase retira os caracteres
    e substitue todos eles por espaço
    str -> str '''
    for caracteres in "-,:;,.~^*&¨%$#@?!":
        frase = frase.replace(caracteres," ")
    return frase