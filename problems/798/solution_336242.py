def freq_palavras(frases):
    
    ''' Função que recebe uma string e retorna um dicionário,
        no qual cada palavra é uma chave cujo valor é o
        número de vezes que a palavra aparece.
        str -> dict '''
    
    dicio = {}
    frase_nova = frase.replace(' ', '/')
    lista = frase_nova.split('/')
    
    for palavra in lista:
        if palavra not in dicio:
            dicio[palavra] = 1
        else:
            dicio[palavra] += 1
            
    return dicio