def freq_palavras(frases):
    
    ''' Função que recebe uma string e retorna um dicionário,
        no qual cada palavra é uma chave cujo valor é o
        número de vezes que a palavra aparece.
        str -> dict '''
    
    dicio = {}
    
    for palavra in frases:
        if palavra not in dicio:
            dicio[palavra] = 1
        else:
            dicio[palavra] += 1
            
    return dicio