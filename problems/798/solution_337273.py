def freq_palavras(frases):
    """Funcao que dada uma frase retorna o numero de vezes que cada palavra
    aparece
    str --> dict"""
    dict = {}
    list = str.split(frases, " ")
    for i in range(len(list)):
        if list[i] in dict:
            dict[list[i]] = dict[list[i]] + 1
        else:
            dict[list[i]] = 1
    return dict