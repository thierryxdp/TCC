def freq_palavras(frase):
    '''
        funcao que receba uma string e retorne um dicionario onde
        cada palavra dessa string seja uma chave e tenha como valor
        o numero de vezes que a palavra aparece.
        dicionario:dict
        frase:str
        lista_palavras:list
        return: dict
        
    '''
    dicionario = {}
    
    lista_palavras = frase.split()
    
    for i in lista_palavras:
        if i not in dicionario:
            dicionario[i] = lista_palavras.count(i)
            
    return dicionario