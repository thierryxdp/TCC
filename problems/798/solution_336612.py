def freq_palavas(frases):
    '''Função que recebe uma string e retorna um dicionário com o número de vezes que cada palavra aparece.'''
    '''str->dict'''
    dicionario = {}
    for i in range(len(frases)):
        frases = str.split(frases)
        
        contador = list.count(frases,frases[i])
        dicionario = dicionario + {frases:contador}
        i = i + 1
    return dicionario