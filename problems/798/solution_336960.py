def freq_palavras(frases):
    """ Função que recebe uma string e retorna um dicionário
    contendo cada palavra da string em questão, sendo que ca-
    da palavra será representada por uma chave e essas chaves
    serão acompanhadas por valores que indicarão quantas ve-
    zes cada palavra apareceu na string.
    
    str -> dict
    """
    
    dicionario = {}
    lista_frases = str.split(frases,)
    for i in lista_frases:
        if i in frases:
            n = list.count(lista_frases, i)
            dicionario[i] = n
    return dicionario