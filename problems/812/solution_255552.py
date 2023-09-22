def retira_pontuacao(texto):
    s=str(texto)
    f=str.replace(s,"...",".")
    return str.strip(f,"?!.-,;:")