def freq_palavras(frase):
    """Função que dada uma frase retorna um dicionário, onde cada palavra é uma chave e tenha como valor
    o número de vezes que a palavra se repete; str -> dict"""
    dicionario={}
    frase = str.split(frase,' ')
    for letra in range(len(frase)):
        if frase[letra] in dicionario:
            dicionario[frase[letra]] += 1
        else:
            dicionario[frase[letra]] = 1
    return dicionario