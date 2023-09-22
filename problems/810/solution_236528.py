def inverte(frase):
    """ """
    frasePontBaixa = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"/"," "),","," "),":"," "),";"," "),"!"," "),"?"," "),"."," "),"-"," ")(str.lower(frase))
    fraseSeparada = str.split (frasePontBaixa)
    fraseInverso = fraseSeparada[len(frase)::-1]
    novaFrase = str.join(" ",(fraseInverso))
    return novaFrase