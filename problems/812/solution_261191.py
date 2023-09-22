def retira_pontuacao(frase):
    frase_nova = str.replace(frase, "-","espaço")
    frase_nova = str.replace(frase,",","espaço")
    frase_nova = str.replace(frase,":","espaço")
    frase_nova = str.replace(frase,";","espaço")
    frase_nova = str.replace(frase,".","espaço")
    return frase_nova