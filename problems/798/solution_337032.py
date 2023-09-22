def freq_palavras(frases:str)->dict:
    '''Calcula a frequência de cada palavra em uma string'''
    palavra = {}
    frases = frases.split()
    for i in frases:
        if i in palavra:
            palavra[i] += 1
        else:
            palavra[i] = 1
    return palavra