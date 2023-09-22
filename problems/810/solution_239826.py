def inverte(texto):
    sub=texto.replace("!", " ").replace("?", "").replace(".", " ").replace(",","").replace(":","").replace(";","").replace("-", " ")
   
    invertida=texto[:-1]
    invtexto=str.join('',invertida)
    return invtexto.lower()