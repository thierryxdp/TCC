def retira_pontuacao(frase):
    pontuacao="." or "!" or "?" or ":" or ";" or "-"
    x=str.replace(frase,pontuacao," ", " ")
    return x