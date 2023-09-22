def lingua_p(x):
    frase=x.lower()
    texto=''
    for i in frase:
        if i in "aeiou":
            texto+=i+'p'+i
        if i not in "aeiou":
            texto+=i
        return texto