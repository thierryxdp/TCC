def inverte(frase):
    frase=frase.replace("!","").replace(",","").replace(":","").replace(";","").replace(".","").replace("?","").replace("!","").replace("-","")
    frase=frase.lower()
    return str.join(" ",str.split(frase," ")[::-1])[1::]