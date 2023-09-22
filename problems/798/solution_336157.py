def req_palavras(frases):
    texto = list(frases)
    dicionario = {}
    for var in frases:
        
        dicionario['var']=str.count(frases,var)
        
    return dicionario