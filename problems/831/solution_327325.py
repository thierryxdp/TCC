def lingua_p(palavra):
    palavra_p = ""
    for letra in palavra:
        if(letra == "a" or letra == "á" or letra == "e" or letra == "é" or letra == "i" or letra == "o" or letra == "u" or letra == "ú"):
            palavra_p = palavra_p + letra +"p" + letra
        else:
            palavra_p = palavra_p + letra
    
    return palavra_p