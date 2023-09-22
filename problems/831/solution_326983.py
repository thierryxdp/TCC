def lingua_p(p):
    """
    função que recebe uma palavra como parâmetro e retorna essa palavra traduzida para a língua do P.
    
    str -> str
    exemplos:
    lingua_p("asa")=="apasapa"
    lingua_p("xoxo")=="xopoxopo"
    lingua_p("lalala")=="lapalapalapa"
	"""
    p=p.lower()
    vogais="aeiouáéíóúãõ"
    for i in p:
        if i in vogais:
            p=p.replace(i,i+"p"+i)
            vogais=vogais.replace(i,"")
    return p