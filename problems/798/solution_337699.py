def freq_palavras(frases):
    '''recebe uma string e retorna um dicionário
    onde cada palavra da string dada é uma chave
    e tem como valor o número de vezes que a pala
    vra aparece.
    str -> dic
    '''
    dicionario = {}
    frase_sep = str.split(frases)
    for palavra in frases:
        dicionario[palavra] = str.count(palavra)
    return dicionario