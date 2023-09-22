def inverte(texto):
    """Função recebe um frase que depois a retorna invertida;
    str->str"""
    texto = str.replace(texto, "!","")
    texto = str.replace(texto, "?","")
    texto = str.replace(texto, ".","")
    texto = str.replace(texto, " ","")
    texto = str.replace(texto, ":","")
    texto = str.replace(texto, ";","")
    texto = str.replace(texto, " "," ")
    v1 = str.split(texto, " ")                    
    v1 = v1[::-1]
    v2 = str.join(" ", v1)
    v3 = str.lower(v2)
    return v3