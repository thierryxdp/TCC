def inverte(frase):
    """frase invertida. Str-->Str"""
    pontuações = ["..." , ".", "!" , "?" , ";" , ":" , "-" , ","]
    frasen=frase.lower()
    frasen= frasen.replace("..." , "")
    frasen= frasen.replace(":" , "")
    frasen= frasen.replace("!" , "")
    frasen= frasen.replace("?" , "")
    frasen= frasen.replace(";" , "")
    frasen= frasen.replace("." , "")
    frasen= frasen.replace("-" , "")
    frasen= frasen.replace("," , "")
    nfrase= str.split(frasen, " ")
    nfrase.reverse()
    return str.join(" " ,nfrase)