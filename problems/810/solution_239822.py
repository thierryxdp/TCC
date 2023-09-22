def inverte(texto):
    sub=texto.replace("!", " ").replace("?", "").replace(".", " ").replace(",","").replace(":","").replace(";","").replace("-", " ")
    normal=str.split(sub(texto),' ')
    invertida=sub[::-1]
    invtexto=str.join('',invertida)
    return invtexto.lower()