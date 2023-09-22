def retira_pontuacao(texto):
    s=str(texto)
    f=str.replace(s,"...",".")
    if str.strip(f,"?!.-,;:")