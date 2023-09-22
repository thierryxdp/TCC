def inverte(frase):
    """ """
    frasePontBaixa = retira_pontuacao(str.lower(frase))
    fraseSeparada = str.split (frasePontBaixa)
    fraseInverso = fraseSeparada[len(frase)::-1]
    novaFrase = str.join(" ",(fraseInverso))
    return novaFrase