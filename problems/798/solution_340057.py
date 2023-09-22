def freq_palavras(frases):
    '''funçao dada uma string conta cada vez que um palavra aparece e coloca num dicionario
    str -> dic'''
    frase = str.split(frases)
    dicionario = {}
    for palavra in frase:
        contador = list.count(frase, palavra)
        dicionario[palavra] = contador
    return dicionario