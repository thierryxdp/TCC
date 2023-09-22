def freq_palavras(frases):
    separacao = frases.split()
    dicionario = {}
    
    for palavra in separacao:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
return dicionario