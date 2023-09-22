def freq_palavras(frases):
    dicio = {}
    n = 1
    frasedit = str.split(frases,' ')
    for palavra in frasedit: ## pra cada palavra na lista
        	dicio[palavra] = str.count(frasedit,palavra)
    return dicio