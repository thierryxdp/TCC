def conta_frases(texto):
    "Retorna o número de frases que aparecem no texto. str->int"
    x = str.split(texto, ".")
    y = str.join(" ",x)
    x1 = str.split(y, "!")
    y1 = str.join(" ",x1)
    x2 = str.split(y1, "?")
    y2 = str.join(" ", x2)
    x3 = str.split(y2, "...")
    y3 = str.join(" ",x3)
    return len(y3)