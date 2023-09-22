def freq_palavras(frases):
    ''' Função que toma uma string e retorna um dicionário onde cada 
    palavra é uma chave que tem como valor o número de vezes que a palavra
    aparece.           str=> dict '''
    contagem = dict()
    palavras = frases.split()

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem