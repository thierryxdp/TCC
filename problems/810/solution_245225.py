def inverte(frase):
    formated = frase.replace("-", " ")
    formated = formated.replace(":", " ")
    formated = formated.replace(";", " ")
    formated = formated.replace(",", " ")
    formated = formated.replace("!", " ")
    formated = formated.replace("?", " ")
    formated = formated.replace("...", " ")
    formated = formated.replace(".", " ")
    
    arrayFrase = formated.split(" ")
    arrayFrase.reverse()
    
    return