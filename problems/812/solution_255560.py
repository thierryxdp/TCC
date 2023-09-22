def retira_pontuacao(texto):
    s=str(texto)
    f=str.replace(s,"...",".")
    g=str.strip(f,"?!.-,;:")
    return str[-1]+" "