def lingua_p(palavra):
    palavra_P = ""
    for i in palavra.lower():
        if i in "áéíóúaeiou":
            palavra_P += i + "p" + i
        else:
            palavra_P += i
    return palavra_P