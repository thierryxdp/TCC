def retira_pontuacao(frase):
    """Retornar a frase incial, porém com espaço substituindo suas pontuações;
    string - > string"""
    frase = frase.replace("!","").replace("?","").replace("...","").replace("-"," ").replace("—","").replace(",","").replace(":","").replace(";","").replace(".","")
    return frase