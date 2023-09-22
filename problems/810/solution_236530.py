def retira_pontuacao(frase):
    """ """
    novaFrase = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"/"," "),","," "),":"," "),";"," "),"!"," "),"?"," "),"."," "),"-"," ")
    return novaFrase



def inverte(frase):
    """ """
    frasePontBaixa = retira_pontuacao(str.lower(frase))
    fraseSeparada = str.split (frasePontBaixa)
    fraseInverso = fraseSeparada[len(frase)::-1]
    novaFrase = str.join(" ",(fraseInverso))
    return novaFrase