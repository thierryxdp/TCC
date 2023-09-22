def retira_pontuacao(frase):
    pontuacao="." or "!" or "?" or ":" or ";" or "-"
    return str.replace(frase,pontuacao," ")