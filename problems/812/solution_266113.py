def retira_pontuacao(frase):
    e = str.replace(frase, "!", " ")
    t = str.replace(frase, "-", " ")
    v = str.replace(frase, ",", " ")
    2p = str.replace(frase, ":", " ")
    pv = str.replace(frase, ";", " ")
    i = str.replace(frase, "?", " ")
    pf = str.replace(frase,".", " ")
    r = str.replace(frase, "...", " ")
    return e + t + v + 2p +  pv + i + e + pf + r