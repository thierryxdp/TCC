def conta_frases(texto):
    """"""
    contagem1 = ()
    contagem2 = ()
    contagem3 = ()
    contagem4 = ()
    
    if "..." in texto:
        contagem1 = str.split(texto,"...")
        del contagem1[1]
    if "." in texto:
        contagem2 = str.split(texto,".")
        contagem2 = contagem2[0:1]       
    if "?" in texto:
        contagem3 = str.split(texto,"?")
        del contagem3[1]
    if "!" in texto:
        contagem4 = str.split(texto,"!")
        del contagem4[1]
        
    contagem_geral = contagem1+contagem2+contagem3+contagem4
    return len(contagem_geral)