def freq_palavras(frases):
    '''Função que recebe uma string e informa quantas vezes a palavra se repetiu'''
    'str-----> dict'
    lista_frases = str.split(frases,' ')
   
    resposta = {}
    for palavra in lista_frases:
        if palavra in resposta:
            resposta[palavra] += 1
        else:
            resposta[palavra] = 1
        return resposta