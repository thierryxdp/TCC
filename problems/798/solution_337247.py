def freq_palavras(frases):
    '''Função que dada uma string, retorna um dicionario onde cada
    palavra dessa string seja uma chave e tenha como valor o número de vezes
    que essa palavra aparece na string.'''
    frase_separada = frases.split()
    i = 0
    dicionario = {}
    j = 1
    
    for i in range(len(frase_separada)):
        
        if frase_separada[i] not in dicionario:
            dicionario[frase_separada[i]] = j
        
        if frase_separada[i] in dicionario:
            dicionario[frase_separada[i]] = +1
        
        
        
       
            
        
        
       
            
    return dicionario