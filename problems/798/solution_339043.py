def freq_palavras(frases):
    '''funcao que retorna um dicionario que conte, uma string como chave e o numero de ocorrencias da string como valor str -> dict'''
    
    dicionario = {}
    
    palavras = str.split(frases)
    
    for palavra in palavras:
        
        ocorrencias = list.count(palavras,palavra)
        
        dicionario[palavra] = ocorrencias
        
    return dicionario