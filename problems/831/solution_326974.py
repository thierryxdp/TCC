def lingua_p(palavra):
    fraseNew = ""
    x=0
    vogais = "a","e","i","o","u","á","é","í","ó","ú"
    for i in palavra:
        if i in vogais:
            fraseNew=fraseNew+i+"p"
        fraseNew = fraseNew + i
    return fraseNew