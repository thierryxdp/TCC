def inverte(frase):
    susbt_ponto = frase.replace(".","")
    susbt_virgula = susbt_ponto.replace(",","")
    susbt_exclamacao = susbt_virgula.replace("!","")
    susbt_interrogacao = susbt_exclamacao.replace("?","")
    susbt_ponto_virguala = susbt_interrogacao.replace(";","")
    susbt_dois_pontos = susbt_ponto_virguala.replace(";","")
    susb_traco = susbt_dois_pontos.replace("-"," ")
    diminuir=str.lower(susb_traco)
    separar = str.split(diminuir)
    list.reverse(separar)
    return separar