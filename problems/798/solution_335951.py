def freq_palavras(frases):
    '''Função que dada uma frase, retorna um dicionario com o numero de vezes que uma palavra aparece na frase'''
    '''str -> dic'''
    fraseMod = frases.split()
    i = 0
    contaFrases = {}
    for valor in fraseMod:
        if valor in contaFrases:
            contador = contaFrases[valor]
            contaFrases[valor] = contador + 1
        else:
        	contaFrases[valor] = 1
    return contaFrases