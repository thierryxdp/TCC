def freq_palavras(frases):
    '''Função que conta a quantidade de vezes que a palavra
    aparece na string frase
    entrada=string
    saida= dicionário'''
    lista=frases.split()
    dicionario={}
    
    for obj in lista:
        if obj in dicionario:
            dicionario[obj] = dicionario[obj] +1
        else:
            dicionario[obj]= 1
    return dicionario