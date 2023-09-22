def retira_pontuacao(frase):
    """ essa função tem como finalidade trocar todos os caracteres de pontuação sejam substituidos por espaço " ",
    entrada -> string
    saida -> string """
    i = str.find(frase, "?")
    e = str.find(frase, "!")
    p = str.find(frase, ".")
    r = str.find(frase, "...")
    dp = str.find(frase, ":")
    pv = str.find(frase, ";")
    t = str.find(frase, "-")
    v = str.find(frase, ",")
    if v != -1:
        frase = str.replace(frase, ",", " ")
    if i != -1:
        frase = str.replace(frase, "?", " ")
    if e != -1:
        frase = str.replace(frase, "!", " ")
    if p != -1:
        frase = str.replace(frase, ".", " ")
    if r != -1:
        frase = str.replace(frase, "...", " ")
    if dp != -1:
        frase = str.replace(frase, ":", " ")
    if pv != -1:
        frase = str.replace(frase, ";", " ")
    if t != -1:
        frase = str.replace(frase, "-", " ")
    return frase