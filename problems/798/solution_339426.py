def freq_palavras(frases):
    ''' função que recebe uma string e retorna um dicionario
    onde cada palavra dessa string seja uma chave e tenha
    como valor o numero de vezes que esssa palavra aparece;
    string->dic'''
    dicionario={}
    for i in frases:
        contador=frases.split().count(i)
        dicionario.update({i:contador})
    return dicionario