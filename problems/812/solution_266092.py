def retira_pontuacao():
    x = str.replace(frase, "...", "")
    x = str.replace(x, "?", "")
    x = str.replace(x, "!", "")
    x = str.replace(x, ".", "")
    x = str.replace(x, ":", "")
    x = str.replace(x, ":", "")
    x = str.replace(x, "-", "")
    x = str.replace(x, ",", "")
    return x