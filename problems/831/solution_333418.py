def lingua_p(palavra):
    """funcao que recebe como parametro uma palavra e retorna essa mesma palavra traduzida
    para a lingua do P.;
    str->str"""
    minusc = palavra.lower()
    novapalavra = ""
    vogais = "aeiouáàéèíìóòúù"
    for p in minusc:
        novapalavra += p
        if p in vogais:
            novapalavra += "p" + p
            
    return novapalavra