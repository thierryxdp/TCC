def retira_pontuacao(frase):
    frase = str.replace(frase, "."," ")
    frase = str.replace(frase, "!", " ")
    frase = str.replace(frase, "?", " ")
    frase = str.replace(frase, ",", " ")
    frase = str.replace(frase, ";", " ")
    frase = str.replace(frase, "-", " ")
    return frase
def inverte(frase):
    Tirar = retira_pontuacao(frase)
    FMin = removePontos.lower()
    TirarEspacos = FMin.strip()
    NovaFrase = TirarEspacos.split()[::-1]
    NovaFrase2 = " ".join(NovaFrase)
    return NovaFrase2