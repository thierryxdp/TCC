def freq_palavras(frase):
    '''Funcao recebe uma afrase e retorna um dicionario com o numero de vezes que cada frase repetiu na frase
    string -> dict'''
    dicionario = {}
    novaFrase = str.split(frase)
    
    for i in novaFrase:
        if  (i in  dict.keys(dicionario)):
            dicionario[i] = dict.get(dicionario, i) + 1
        else:
            dicionario[i] = 1
    return dicionario