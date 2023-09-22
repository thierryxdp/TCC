def retira_pontuacao(frase):
    "..."
     if "-" or "," or ":" or ";" or "!" or "?" or "." in x:
            a = str.replace(x, "-", " ")
            b = str.replace(a, ",", " ")
            c = str.replace(b, ":", " ")
            d = str.replace(c, ";", " ")
            e = str.replace(d, "!", " ")
            f = str.replace(e, "?", " "):
                return str.replace(f, ".", " ")