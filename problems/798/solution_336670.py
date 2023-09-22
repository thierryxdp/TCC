def freq_palavras(frases):
    """Dada uma string de entrada, a função retorna um dicionário com
    o número de ocorrências de cada palavra, onde cada palavra da string
    é uma chave do dicionário e seu valor é o número de vezes que essa 
    palavra aparece.
    str -> dict"""
    
    dicionario = {}
    palavras = str.split(frases)
    
    for palavra in palavras:
        
        if palavra not in dict.keys(dicionario):
            dicionario[palavra] = 1
            
        elif palavra in dict.keys(dicionario):
            dicionario[palavra] += 1
            
    return dicionario