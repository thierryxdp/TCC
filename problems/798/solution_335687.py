def freq_palavras(frases):
    """Função que, dada uma string, retorna um dicionário onde cada palavra dessa string é uma chave e tem como valor o número de vezes que a palavra aparece; str->dicionário"""
    
    palavras = str.split(frases)
    i = 0
    lista = []
    dicionario = []
    
    while i < len(palavras):
        
        lista = lista + [list.count(palavras,palavras[i])]
        
        i = i + 1
        
    i = 0    
        
    for x in lista:
        
        dicionario = dicionario + [palavra[i],lista[i]]
                      
        i = i + 1
        
    return dicionario