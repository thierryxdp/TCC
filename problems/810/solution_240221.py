def inverte(frase):
    susbt_ponto = frase.replace(".","*")
    susbt_virgula = susbt_ponto.replace(",","*")
    susbt_exclamacao = susbt_virgula.replace("!","*")
    susbt_interrogacao = susbt_exclamacao.replace("?","*")
    susbt_ponto_virguala = susbt_interrogacao.replace(";","*")
    susbt_dois_pontos = susbt_ponto_virguala.replace(";","*")
    susb_traco = susbt_dois_pontos.replace("-","*")
    remove = str.split(susb_traco,"*")
    frase = remove[0:-1]
    list.reverse(frase)
    return frase