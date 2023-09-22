def freq_palavras(frase):
    dicionario = {}
    lista = string.split()
    
    for i in lista:
        if(i in dicionario):
            dicionario[i] += 1 
        else:
            dicionario[i] = 1
    
    return dicionario