def lingua_p(palavra):
    """  """

    npalavra = palavra.lower()
    vogais = [a,e,i,o,u]
    resposta = ""

    for i in vogais:
        npalavra = npalavra.split(i)

        for j in npalavra:
        	resposta = resposta + j + i + "p" + i

    return resposta