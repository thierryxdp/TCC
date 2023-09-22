def conta_frases(frase):
    """
    str->int
    :param frase: Uma frase que terá um caracter final
    :return: O numero de caracteres especiais que a frase apresenta
    """
    n=0
    elm=0
    for el in frase:
        elm+=1
        if  el == "." :
            if frase[elm-2] != ".":
                n+=1
                
        elif el == "!" or el == "?":
            n+=1
            return n
 	return n