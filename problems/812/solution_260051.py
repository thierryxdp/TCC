def retira_pontuacao(texto):
    if "-" or "," or ":" or ";" or "." in texto:
        "-"=" "
        ","=" "
        ":"=" "
        ";"=" "
        "."=" "
        return texto