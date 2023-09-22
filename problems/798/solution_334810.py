def freq_palavras(frases):
    '''Fazer uma funcao que receba uma string e retorne um dicionario que cada palavra seja uma chave e mostre quantas vezes ela aparece;
    string -> dict'''
    
    parte = str.split(frase)
    final = {}
    
    for palavra in parte:
        uma = list.count(parte,palavra)
        final[palavra] = uma
        
    return final