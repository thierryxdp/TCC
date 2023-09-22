def uppCons(texto):
   #receba como entrada uma frase e retorne a frase com todas as suas consoantes em maiúsculas; String => String#
    i=0
    texto = list(texto)
    while i<len(texto):
        if texto[i].upper() in 'BHCDFGJKLMNPQRSTVWXYÇZ':
            texto[i] = texto[i].upper()
        i=i+1
    texto = ''.join(texto)
    return texto