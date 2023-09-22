def freq_palavras(frases):
    """ Função que recebe uma string e retorna um dicionario onde a chave de cada string sera as vezes no qual se repete. input string, return dict """

    dicionario = {}
    x = frases.split()
    
    for i in x:
        if i not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    return dicionario