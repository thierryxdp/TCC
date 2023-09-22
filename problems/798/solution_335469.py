def freq_palavras(frases):
    lista=frases.split()
    dicionario={}
    
    for obj in lista:
        if obj in dicionario:
            dicionario[obj] = dicionario[obj] +1
        else:
            dicionario[obj]= 1
    return dicionario