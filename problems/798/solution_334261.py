def freq_palavras(frases):
    """Recebe uma frase e retorna um dicionário contendo cada palavra e o seu
    numero de ocorrências

    str -> dict"""
    dic = {}
    lista_frase = frases.split(' ')
    for i in lista_frase:
        dic[i] = lista_frase.count(i)
    return dic