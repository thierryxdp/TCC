def lingua_p(palavra):
    palavra_P = ""

    for i in palavra:
        if i in "áéíóúaeiouAEIOU":
            palavra_P += i.lower() + "p" + i.lower()
        else:
            palavra_P += i.lower()
    return palavra_P.lower()