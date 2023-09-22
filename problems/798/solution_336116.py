def freq_palavras(frases):
    '''
    	Função que recebe uma string e 
        retorna um dicionário cujas 
        chaves são palavras da string e
        cujos valores são o número de
        vezes que cada palavra aparece
        : param frases: string
        : return: dict
    '''
    lista = str.split(frases,' ')
    dicio = {}
    
    for palavra in lista:
        if palavra not in dicio:
            dicio[palavra] = list.count(lista,palavra)
            
    return dicio