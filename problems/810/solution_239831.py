def inverte(texto):
    sub=texto.replace("!", " ").replace("?", "").replace(".", " ").replace(",","").replace(":","").replace(";","").replace("-", " ")
    frase=str.split(sub)
    invertida=sub[::-1]
    
    return invertida.lower()