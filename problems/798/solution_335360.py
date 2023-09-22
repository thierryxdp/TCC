def freq_palavras(frase):
    """recebe uma frase e retorna um dicionario no qual cada palavra dessa 
    frase e uma chave, e a quantidade de vezes em que cada uma aparece sao 
    os valores
    string -> dictionary"""
    
    palavras = str.split(frase)
    dicionario = {}
    
    for i in range(len(palavras)):
        repeticoes = list.count(palavras, palavras[i])
        dicionario[palavras[i]] = repeticoes
        
    return dicionario