def freq_palavras (frases: str)-> dict:
    '''Retorna um dicionário onde cada palavra da string dada seja uma chave
    e tenha como valor o número de vezes que aparece'''
    str.replace(frases,' ',',')
    str.replace(frases,'.',',')
    str.split(frases,',' )
    dicionario = {}
    for elem in frases:
        dicionario[elem]=0
    for elem in frases:
        dicionario[elem]= dicionario[elem] + 1
    return dicionario