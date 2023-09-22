def lingua_p(palavra):
    palavra_p = ""
    for letra in palavra:
        if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
            palavra_p.append(letra +"p" + letra)
        else:
            palavra_p.append(letra)
    
    return palavra_p