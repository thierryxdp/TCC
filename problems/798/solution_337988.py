def freq_palavras(frases):
    '''
    	Função que recebe uma string e retorna um dicionário onde
        cada palavra dessa stringa é uma chave e tenha como valor o 
        número de vezes que a pálavra aparece.
        str -> dict
    '''
    dicionario = {}
    frase_separada = str.split(frases)
    
    for x in range(len(frase_separada)):
        if frase_separada[x] not in dicionario:
        	dicionario[frase_separada[x]]= list.count(frase_separada, frase_separada[x])
        
    return dicionario