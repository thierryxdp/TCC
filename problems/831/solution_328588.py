def ligua_p(palavra):
    #texto = input("Digite um texto: ")

    for c in "aeiou":
        palavra = palavra.replace(c, c+'p')
    return palavra