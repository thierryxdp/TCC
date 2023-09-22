def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece
    entrada: string
    saída: dict"""
    dicionario={}
    for palavra in frases:
        if palavra in dicionario:
            dicionario=dicionario+{palavra:+=1}
        else:
            dicionario=dicionario+{palavra:1}
    return dicionarios