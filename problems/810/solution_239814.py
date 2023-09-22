def inverte(texto):
    sub=texto.replace("!", "").replace("?", "").replace(".", "").replace(",","").replace(":","").replace(";","").replace("-", "")
    invertida=sub[::-1]
    invtexto=str.join('',invertida)
    return invtxt.lower()