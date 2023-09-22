def retira_pontuacao(frase):
    """Essa funcao recebe 'frase' str -> str
substitui as pontuacoes utilizando a funcao replace
de str"""
    frase = str.replace(frase, "-", " ")
    frase = str.replace(frase, ",", "")
    frase = str.replace(frase, ":", "")
    frase = str.replace(frase, ";", "")
    frase = str.replace(frase, ".", "")
    frase = str.replace(frase, "!", "")
    frase = str.replace(frase, "?", "")
    frase = str.replace(frase, "...", "")
    
    return frase

def inverte(frase):
    frase = retira_pontuacao(frase).lower()
    lista = str.split(frase, " ")
    lista = lista[::-1]
    return str.join(" ", lista)