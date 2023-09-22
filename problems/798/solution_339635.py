def freq_palavras(frase):
    dicionario = {}
    lista = frase.split()
    
    for i in lista:
        if(i in dicionario):
            dicionario[i] += 1 
        else:
            dicionario[i] = 1
    
    return dicionario