def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário onde cada palavra dessa string é uma chave e tem como valor o número de vezes que a palavra aparece
    str -> dict"""
    contador = 0
    conta_palavras = {}
    separador = str.split(frases)
    for x in range(len(separador)):
        z = separador[y]
        conta_palavras[z] = list.count(separador, separador[contador])
        contador = contador + 1    
    return conta_palavras