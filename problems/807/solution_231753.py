def conta_frases(frase):
    fim = {"." : "JJJ", "!" : "JJJ", "?" : "JJJ", "..." : "JJJ" }
    return (str.count(frase, "JJJ"))