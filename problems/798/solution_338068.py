def freq_palavras(frases):
    '''
       Dada uma frase a função retorna um dicionário contendo
       cada palavra da frase como chave e o valor é igual a
       quantidade de vezes que a palavra aparece na frase
       str -> dict
    '''
    ocorrencias={}
    for i in frases:
        if i in ocorrencias:
            ocorrencias[i] = ocorrencias[i] + 1
        else:
            ocorrencias[i] = 1
    return ocorrencias