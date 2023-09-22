def freq_palavras(frases):
    """dada uma string frase retorna um dicionário que possui como chaves
    as palavras dessa frase e como valores a quantidade de vezes que a frase
    se repete
    str --> dict"""
    lista_frases=str.split(frases,' ')
    palavras_rep={}
    for palavra in lista_frases:
        if palavra in palavras_rep:
            palavras_rep[palavra]=palavras_rep[palavra]+1
        if palavra not in palavras_rep:
            palavras_rep[palavra]=1
    return palavras_rep