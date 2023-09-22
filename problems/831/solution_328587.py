def ligua_p(texto):
    #texto = input("Digite um texto: ")

    for c in "aeiou":
        texto = texto.replace(c, c+'p')
    return texto