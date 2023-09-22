def freq_palavras (frases):
    """Função que recebe um string e ira retornar um dicionario
    onde as palavras são chaves e o valor será o número de vezes
    que a palavra aparece. str -> dict"""
    palavras = " "
    for nvezes in frase:
        if nvezes in dicionario:
            palavras = palavras + nvezes
    return palavras