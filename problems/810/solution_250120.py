def inverte(x=""):
    ''' função que iverte a ordem das palavras numa frase
    str>>str'''
    x=x.replace(".","").replace(";","").replace(",","").replace("-"," ").replace(":","").replace("?","").replace("!","").replace("/","").lower()
    x=x.split(" ")
    return str(" ").join(x[::-1])