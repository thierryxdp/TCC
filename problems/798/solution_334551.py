def freq_palavras(frases):
    
    '''Função que recebe uma frase e retorna um dicionário com a quantidade de vezes que cada palavra aparece. str -> dict'''
    
    lista = str.split(frases)
    dicio = {}
    
    for i in lista:
        dicio[i] = list.count(lista,i)
        
    return dicio