def retira_pontuacao(frase):
    """Determinar a frase de entrada, porém com espaço substituindo suas pontuações;
    string - > string"""
    frase = frase.replace("!","").replace("?","").replace("...","").replace("-"," ").replace("—","").replace(",","").replace(":","").replace(";","").replace(".","")
    return frase