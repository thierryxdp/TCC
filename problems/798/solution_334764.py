def freq_palavras(frase):
    '''função recebe frase e retorna dicionário com
    quantidade de cada palavra da string
    str--> dict'''

    lista_palavras = frase.split()
    dict1 = {}
    contador = 0

    for palavra in lista_palavras:
        dict1[lista_palavras[contador]] = lista_palavras.count(lista_palavras[contador])
        contador += 1

    return dict1