def freq_palavras (frases):
    """a seguinte função irá receber a frase e retornar um dicionário com a
    quantidade de cada palavra da string  str--> dict"""
    lista_palavras = frase.split()
    dict1 = {}
    contador = 0
    for palavra in lista_palavras:
    dict1[lista_palavra[contador]] = lista_palavras.count(lista_palavras[contador])
    contador += 0
    return dict1