def retira_pontuacao(frase):
    return str.join(" ", str.split(frase,"-" or "," or ":" or ";" or "." or "?"or "!"))