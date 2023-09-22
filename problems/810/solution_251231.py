def retira_pontuacao(frase):
    """Retorne a frase de entrada, porém com espaço substituindo suas pontuações;
    string - > string"""
    frase = frase.replace("!","").replace("?","").replace("...","").replace("—","").replace(",","").replace(":","").replace(";","").replace(".","")
    return frase

def inverte(frase):
    """Retorne a frase de entrada, porém toda minuscula, sem pontuações e com a ordem inversa;
    string - > string"""
    frases = retira_pontuacao(frase).lower().split(" ")[::-1]
    return " ".join(frases)