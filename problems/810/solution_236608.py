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
    if v != -1:
        frase = str.replace(frase, ",", " ")
    return frase
def inverte(frase):
    """ essa função alem de tirar todos os sinais de pontuação, ainda inverte as palavras na ordem inversa sem letras maiusculas
    entrada -> str
    saida -> str """
    
    frase = retira_pontuacao(frase)
    frase2 = str.split(frase)
    frase3 = frase2[::-1]
    return str.lower(str.join(" ", frase3))