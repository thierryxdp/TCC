def retira_pontuacao(frase):
    #Essa função retorna uma frase com as mesmas palavras mas com ordem invertida
    #A frase não possui letras maiúsculas e pontuação
    frase = str.replace(frase, "."," ")
    frase = str.replace(frase, "!", " ")
    frase = str.replace(frase, "?", " ")
    frase = str.replace(frase, ",", " ")
    frase = str.replace(frase, ";", " ")
    frase = str.replace(frase, "-", " ")
    return frase
def inverte(frase):
    Tirar = retira_pontuacao(frase)
    FMin = Tirar.lower()
    TirarEspacos = FMin.strip()
    NovaFrase = TirarEspacos.split()[::-1]
    NovaFrase2 = " ".join(NovaFrase)
    return NovaFrase2