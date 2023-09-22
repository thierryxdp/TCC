def freq_palavras(frases):
    '''
       Dada uma frase a função retorna um dicionário contendo
       cada palavra da frase como chave e o valor é igual a
       quantidade de vezes que a palavra aparece na frase
       str -> dict
    '''
    ocorrencias={}
    palavra = frases.split()
    for palavra in frases.split():
        if palavra in ocorrencias:
            ocorrencias[palavra] = ocorrencias[palavra] + 1
        else:
            ocorrencias[palavra] = 1
    return ocorrencias