def retira_pontuacao(frase):
    str.replace(frase, "-","espaço")
    str.replace(frase,",","espaço")
    str.replace(frase,":","espaço")
    str.replace(frase,";","espaço")
    str.replace(frase,".","espaço")
    return frase