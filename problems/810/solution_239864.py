def inverte(texto):
    sub=texto.replace("!", " ").replace("?", "").replace(".", " ").replace(",","").replace(":","").replace(";","").replace("-", " ")
    normal=str.split(sub(frase),'')
    frase=str.split(sub)
    invfrase=str.join(' ',frase)
    invertida=invfrase[:-1]
    
    return normal