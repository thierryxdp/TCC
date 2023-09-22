def freq_palavras(frases):
    '''Função que recebe uma string e retorna um dicionário onde cada palavra da string seja uma chave;
    e possua como valor o número de vezes que a palavra aparece;
    str -> dict'''
    nfrases = frases.split()
    dicionario = {}
    i =1
    
    for palavra in nfrases:
        if palavra not in dicionario:
            dicionario = {dicionario, palavra:i, }
        elif palavra in dicionario:
            i+=1
            dicionario = {dicionario, palavra:i, }
    return dicionario