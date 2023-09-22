def inverte(frase):
    formated = frase.replace("-", " ")
    formated = formated.replace(":", " ")
    formated = formated.replace(";", " ")
    formated = formated.replace(",", " ")
    formated = formated.replace("!", " ")
    formated = formated.replace("?", " ")
    formated = formated.replace("...", " ")
    formated = formated.replace(".", " ")
    formated = formated.lower()
    
    arrayFrase = formated.split(" ")
    arrayFrase.reverse()
    
    return " ".join(arrayFrase)