def inverte(texto):
    sub=texto.replace("!", " ").replace("?", "").replace(".", " ").replace(",","").replace(":","").replace(";","").replace("-", " ")
    frase=str.split(sub)
    invfrase=str.join('',frase)
    invertida=frase[::-1]
    
    return invfrase