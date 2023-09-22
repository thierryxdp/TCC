def freq_palavras(frases):
    '''
    funcao que recebe uma string e retorna um dicionario
    onde cada palavra da string e uma chave do dicionario
    e os valores o numero de vezes que a palavra aparece
    string -> dicio
	'''

    
    i = 0
    dicio = {}
    chaves = frase.split()
    for i in range(len(chaves)):
        
        valor = chaves.count(chaves[i])
        dicio[chaves[i]] = valor
        i = i +1 

    return dicio