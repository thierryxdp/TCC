def inverte(frase):
    """ """
    s = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"/"," "),","," "),":"," "),";"," "),"!"," "),"?"," "),"."," "),"-"," ")
    frasePontBaixa = s(str.lower(frase))
    fraseSeparada = str.split (frasePontBaixa)
    fraseInverso = fraseSeparada[len(frase)::-1]
    novaFrase = str.join(" ",(fraseInverso))
    return novaFrase