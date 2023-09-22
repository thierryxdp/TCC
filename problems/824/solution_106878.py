def uppCons (frase):
    for elem in "b c d f g h j k l m n p q r s t v w x z":
        frase = frase.replace(elem, elem.upper())
    return frase