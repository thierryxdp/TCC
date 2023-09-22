def freq_palavras(frases):
    """Essa função retorna um dicionario onde cada 
    palavra de uma string dada e um chave e o numero 
    de repetições dessas palavras e o seu valor.
    string -> dicionario"""
    
    palavras = str.split(frases, " ")
    list.sort(palavras)
    dicionario=dict()
    
    for i in range(len(palavras)):
        
        item = palavras[i]
        ocorrencia = list.count(palavras, item)
        dicionario[item] = ocorrencia
                    
    return dicionario