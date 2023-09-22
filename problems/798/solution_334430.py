def freq_palavras (frase):
    '''recebe uma string e retorna um dicionario com o número de vezes em que essa palavra aparece'''
    '''str->dicionario'''
    i = 0
    final = []
    for nome in frase:
        if nome in frase:
            um = str.count(frase, nome[i])
            final = {frase[i]:um,}
            
        i = i+1
    return final